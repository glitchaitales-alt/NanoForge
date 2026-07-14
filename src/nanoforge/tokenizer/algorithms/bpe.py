from collections import Counter
from collections.abc import Iterable
from ..merge_rule import MergeRule

class BPETrainer:

    def __init__(self) -> None:
        self.merges: list[MergeRule] = []
        self._next_token_id = 256


    def count_pairs( 
        self,
        corpus: Iterable[list[int]],
    ) -> Counter[tuple[int, int]]:

        counts = Counter()

        for word in corpus:
            for left, right in zip(word, word[1:]):
                counts[(left, right)] += 1

        return counts

    def most_frequent_pair(
        self,
        counts: Counter[tuple[int, int]],
    ) -> tuple[int, int] | None:
        """
        Return the most frequent pair.

        Returns None if no pairs exist.
        """

        if not counts:
            return None

        return counts.most_common(1)[0][0]
    

    def merge_pair(
        self,
        corpus: list[list[int]],
        pair: tuple[int, int],
        new_token: int,
    ) -> list[list[int]]:
        """
        Merge every occurrence of a pair in the corpus.
        """

        merged_corpus = []

        left, right = pair

        for word in corpus:

            merged_word = []

            i = 0

            while i < len(word):

                if (
                    i < len(word) - 1
                    and word[i] == left
                    and word[i + 1] == right
                ):
                    merged_word.append(new_token)
                    i += 2

                else:
                    merged_word.append(word[i])
                    i += 1

            merged_corpus.append(merged_word)

        return merged_corpus
    
    
    def train(
        self,
        corpus: list[list[int]],
        num_merges: int,
    ) -> list[list[int]]:
        self.merges.clear()
        self._next_token_id = 256
        corpus = [word[:] for word in corpus]

        for _ in range(num_merges):

            counts = self.count_pairs(corpus)

            pair = self.most_frequent_pair(counts)

            if pair is None:
                break

            merged = self._next_token_id

            self._next_token_id += 1

            left, right = pair

            self.merges.append(
                MergeRule(
                    left=left,
                    right=right,
                    merged=merged,
                )
            )

            corpus = self.merge_pair(
                corpus,
                pair,
                merged,
            )

        return corpus