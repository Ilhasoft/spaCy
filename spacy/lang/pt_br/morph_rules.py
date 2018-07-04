# coding: utf8
from __future__ import unicode_literals

from ...symbols import LEMMA, PRON_LEMMA

MORPH_RULES = {
    "PRP": {
        "eu": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "você": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "tu": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "ele": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "ela": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "nós": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "vós": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "eles": {LEMMA: PRON_LEMMA, "PronType": "Prs"},
        "elas": {LEMMA: PRON_LEMMA, "PronType": "Prs"}
    }
}