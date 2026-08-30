# Pré-enregistrement S2 (référence hub)

> Document figé avant campagne provider réelle.
> Source de vérité opérationnelle : repo hub AION- / preenregistrement.json

## Hypothèses

- **H0** : AION n'améliore pas le BAR au-delà de l'étendue de mesure vs SCAFFOLD (même modèle).
- **H1** : AION dépasse SCAFFOLD d'un écart > somme des étendues, sur ≥3 familles dont `repeated_error` et `stale_knowledge`.

## Seuils (réf.)

- Δ(AION − RAW) minimum : **0.15**
- FSR maximum : **0.15**
- Entrée référence : paraphrase + extracteur llm (protocole S2)
- Reps : 20 · Cas : 20 (noyau) / 100 (aion-100 étendu)

## Statut

FROZEN côté méthode. Toute modification post-résultat invalide la campagne.
