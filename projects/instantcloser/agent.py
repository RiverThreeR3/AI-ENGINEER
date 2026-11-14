"""Public, independent InstantCloser decision-policy teaching lab.

This is NOT the production InstantCloser code. No network calls, PII, CRM writes,
messages, bookings or payments are performed here.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
import unicodedata


@dataclass(frozen=True)
class LeadRequest:
    tenant_id: str
    message: str
    consent_to_contact: bool = False
    active_objection: bool = False


@dataclass(frozen=True)
class Decision:
    action: str
    reason: str
    needs_model_review: bool = False
    requires_approval: bool = False
    external_action_executed: bool = False


def _normalize(message: str) -> str:
    plain = unicodedata.normalize("NFKD", message.casefold())
    return "".join(ch for ch in plain if not unicodedata.combining(ch))


def _has_any(message: str, phrases: tuple[str, ...]) -> bool:
    return any(re.search(r"(?<!\w)" + re.escape(p) + r"(?!\w)", message) for p in phrases)


def decide(request: LeadRequest) -> Decision:
    """Return the next *proposed* action, never execute one."""
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,64}", request.tenant_id):
        raise ValueError("tenant_id must be a nonempty safe identifier")
    if not isinstance(request.message, str):
        raise ValueError("message must be a string")
    if not 1 <= len(request.message) <= 2000:
        raise ValueError("message length must be 1..2000 characters")
    message = _normalize(request.message)

    # Highest-priority controls: a buyer's refusal and attempted instruction override.
    if _has_any(message, ("nao me contate", "nao quero receber contato", "pare de mandar", "stop contacting", "unsubscribe", "opt out")):
        return Decision("do_not_contact", "Explicit opt-out overrides sales optimization.")
    if _has_any(message, ("ignore previous instructions", "ignore all rules", "ignore suas instrucoes", "system prompt", "developer message")):
        return Decision("security_review", "Untrusted buyer text cannot override the policy.", requires_approval=True)
    if not request.consent_to_contact:
        return Decision("request_consent", "Permission to contact is not recorded.")
    if request.active_objection or _has_any(message, ("muito caro", "too expensive", "nao confio", "not interested")):
        return Decision("clarify_objection", "Resolve buyer concerns before proposing a close.")
    if _has_any(message, ("agendar", "marcar", "schedule", "book", "appointment")):
        return Decision("propose_slots", "Buyer requested scheduling; booking is not confirmed.", requires_approval=True)
    if _has_any(message, ("preco", "quanto custa", "valor", "price", "pricing", "cost")):
        return Decision("request_approved_pricing", "Quote only tenant-approved pricing; none is loaded in this lab.")
    if _has_any(message, ("comprar", "buy", "purchase", "fechar negocio")):
        return Decision("confirm_purchase_intent", "Purchase needs an explicit, authorized next step.", requires_approval=True)
    return Decision("request_clarification", "Deterministic parser found no supported intent.", needs_model_review=True)
