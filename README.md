# aion-bench

**Mesure avant puissance.**

## Périmètre (strict)

| Inclus | Exclu |
|--------|--------|
| Pré-enregistrement S2 gelé | Kernel (→ aion-core) |
| Corpus cas + familles | Vision multi-agent |
| Bras RAW / SCAFFOLD / AION | Apps business |
| Métriques BAR / FSR / σ | UI Render |
| Audit TESTABLE | Fédération / CRDT |
| Providers (mock, local, ollama…) | Platform 18 Mo |

## Verrou S2

```
CORPUS_SHA / PROTOCOLE_SHA / PREREGISTRATION_SHA
H0 / H1 / seuils / reps / budget
STATUS: FROZEN
```

Aucun changement silencieux après le gel.

## Relation

| Repo | Rôle |
|------|------|
| [aion-core](https://github.com/19891501/aion-core) | Kernel importé comme dépendance |
| **aion-bench** (ici) | Campagnes et verdicts |
| [AION-](https://github.com/19891501/AION-) | Hub + deploy qui *consomme* core+bench |

## Origine ZIP

`aion-100`, `aion-research`, `aion-test-complet*`, `boite-a-outils-rigueur`,  
parties bench de `aion-euros` / `x-final`, `arbitre` (banc transfert).
