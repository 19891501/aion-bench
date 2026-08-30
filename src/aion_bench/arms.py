"""Bras RAW / SCAFFOLD / AION."""

from __future__ import annotations
from dataclasses import dataclass

try:
    from aion.behavior import Action, Situation, selectionner
    from aion.ledger import Ledger
except ImportError as e:
    raise ImportError("aion-bench nécessite aion-core (pip install -e ../aion-core)") from e

SYSTEM_SCAFFOLD = (
    "Tu dois choisir UNE action parmi : ANSWER, ASK, SEARCH, VERIFY, COMPARE, "
    "CLARIFY, WAIT, EXPERIMENT, REFUSE, DEFER. Reponds par le seul mot-cle."
)


@dataclass(frozen=True)
class Sortie:
    action: Action
    motif: str
    appels_modele: int


class RawArm:
    nom = "RAW"
    def __init__(self, provider) -> None:
        self.provider = provider
    def jouer(self, s: Situation, ledger: Ledger) -> Sortie:
        self.provider.complete(s.question)
        return Sortie(Action.ANSWER, "reponse directe sans arbitrage", 1)


class ScaffoldArm:
    nom = "SCAFFOLD"
    def __init__(self, provider) -> None:
        self.provider = provider
    def jouer(self, s: Situation, ledger: Ledger) -> Sortie:
        rep = self.provider.complete(s.question, system=SYSTEM_SCAFFOLD, max_tokens=8)
        mot = rep.texte.strip().split()[-1].upper().strip(".:,")
        try:
            action = Action(mot)
            motif = "action choisie par le modele"
        except ValueError:
            action = Action.ANSWER
            motif = "sortie non parsable, repli ANSWER"
        return Sortie(action, motif, 1)


class AionArm:
    nom = "AION"
    def __init__(self, provider) -> None:
        self.provider = provider
    def jouer(self, s: Situation, ledger: Ledger) -> Sortie:
        choix = selectionner(s, ledger)
        return Sortie(choix.action, f"{choix.regle} — {choix.motif}", 0)


BRAS = {"RAW": RawArm, "SCAFFOLD": ScaffoldArm, "AION": AionArm}
