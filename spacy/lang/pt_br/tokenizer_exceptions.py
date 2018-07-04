# encoding: utf8
from __future__ import unicode_literals
from ...symbols import ORTH


_contacted_words = {}
_contacted_words["às"] = [{ORTH: "à"}, {ORTH: "s"}]
_contacted_words["ao"] = [{ORTH: "a"}, {ORTH: "o"}]
_contacted_words["aos"] = [{ORTH: "a"}, {ORTH: "os"}]
_contacted_words["àquele"] = [{ORTH: "à"}, {ORTH: "quele"}]
_contacted_words["àquela"] = [{ORTH: "à"}, {ORTH: "quela"}]
_contacted_words["àqueles"] = [{ORTH: "à"}, {ORTH: "queles"}]
_contacted_words["àquelas"] = [{ORTH: "à"}, {ORTH: "quelas"}]
_contacted_words["àquilo"] = [{ORTH: "à"}, {ORTH: "quilo"}]
_contacted_words["aonde"] = [{ORTH: "a"}, {ORTH: "onde"}]

TOKENIZER_EXCEPTIONS = dict(_contacted_words)