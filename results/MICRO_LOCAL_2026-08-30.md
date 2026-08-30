# Micro-campagne locale — 2026-08-30

> **NON OPPOSABLE au pré-enregistrement S2**  
> 5 cas × 3 reps · provider=local · entrée=paraphrase · extracteur=lexical

## Objectif

Valider le **circuit de mesure**, pas publier un résultat frontier.

## Résultats

| Bras | BAR moyen | σ | min | max |
|------|-----------|---|-----|-----|
| RAW | 0.200 | 0.163 | 0.00 | 0.40 |
| SCAFFOLD | 0.200 | 0.163 | 0.00 | 0.40 |
| **AION** | **0.533** | 0.189 | 0.40 | 0.80 |

Δ(AION − RAW) ≈ **+0.33** (indicatif, n trop faible, provider non réel).

Empreinte pré-enregistrement (ref) : `d2fc38c0d4146d4181f200e36266582cefd8e32030ff37548a0af9de6c87db77`

## Lecture honnête

1. Le banc **tourne** et différencie les bras.
2. AION > RAW/SCAFFOLD sur cet échantillon — **hypothèse encourageante**, pas preuve S2.
3. Provider `local` : aucun chiffre n’est un résultat modèle frontier.
4. σ élevé + 3 reps : instabilité attendue (déjà analysée).

## Kernel (hors banc)

- Règles R0–R10 échantillon : 7/7 PASS
- Pipeline 10 k€ : `VERIFY → CONFLICT → DEMANDER_HUMAIN`

## Prochaine campagne opposable

```bash
# protocole gelé S2 — provider réel (ollama ou cloud)
aion bench --provider ollama --entree paraphrase --extracteur llm
# reps=20, cas complets, cache on, budget déclaré
```

Statut : **circuit OK · preuve S2 en attente**
