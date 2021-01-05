import re


class BloodSample:

    def __init__(self, sequence):
        self.sequence = sequence.strip()
        self.matched_pattern = []

    def is_valid(self):
        c=re.compile('^[0-1]+$')
        return bool(c.match(self.sequence))

    def parse(self):
        compiled_sequence = re.compile('1[1]+')
        self.matched_pattern = compiled_sequence.findall(self.sequence)
        return self.matched_pattern

    @property
    def number_of_matched(self):
        return len(self.matched_pattern)

    @property
    def list_of_matched(self):
        return list(map(len, self.matched_pattern))
