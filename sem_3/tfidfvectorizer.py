from countvectorizer import CountVectorizer
from tfidftransformer import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    """
    Transform a collection of text documents into a TF-IDF (Term Frequency-Inverse Document Frequency) matrix.

    Methods:
        fit_transform(corpus: List[str]) -> List[List[float]]:
            Transform a corpus of text documents into a TF-IDF matrix.

        transform(corpus: List[str]) -> List[List[float]]:
            Transform a corpus of text documents into a TF-IDF matrix based on the existing vocabulary.

    Attributes:
        lowercase (bool): If True, convert text to lowercase (default is True).
        separator (str): The separator used to split text into words (default is a space).
        stop_chars (str or list[str]): Characters to be removed from the text before processing (default is '.,?!').

    """
    def __init__(
        self,
        lowercase: bool = True,
        separator: str = ' ',
        stop_chars: str | list[str] = '.,?!'
    ) -> None:
        """
        Initialize the TfidfVectorizer.

        :param lowercase: If True, convert text to lowercase (default is True).
        :param separator: The separator used to split text into words (default is a space).
        :param stop_chars: Characters to be removed from the text before processing, either as a string or a list (default is '.,?!').
        """
        super().__init__(lowercase, separator, stop_chars)
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Transform a corpus of text documents into a TF-IDF matrix.

        :param corpus: List of text documents.
        :return: TF-IDF matrix.
        """
        count_matrix = super().fit_transform(corpus)

        return self.tfidf_transformer.fit_transform(count_matrix)

    def transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Transform a corpus of text documents into a TF-IDF matrix based on the existing vocabulary.

        :param corpus: List of text documents.
        :return: TF-IDF matrix.
        """
        count_matrix = super().transform(corpus)

        return self.tfidf_transformer.fit_transform(count_matrix)
