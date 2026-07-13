from collections import Counter
from collections.abc import Iterable


class BPETrainer:

    def count_pairs(
        self,
        corpus: Iterable[list[str]],
    ) -> Counter[tuple[str, str]]:

        counts = Counter()

        for word in corpus:

            for i in range(len(word) - 1):

                pair = (
                    word[i],
                    word[i + 1],
                )

                counts[pair] += 1

        return counts