class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.

    Attributes:
        lowercase (bool): If True, convert text to lowercase (default is True).
        separator (str): The separator used to split text into words (default is a space).
        stop_chars (str or list[str]): Characters to be removed from the text before processing
            (default is '.,?!').

    Methods:
        remove_chars(document: str) -> str:
            Remove specified characters from the given document.

        split_document(document: str) -> list[str]:
            Split a document into a list of words, with optional preprocessing.

        fit(corpus: list[str]) -> None:
            Build the vocabulary from a corpus of documents.

        transform(corpus: list[str]) -> list[list[int]]:
            Transform a corpus of documents into a term-document matrix.

        fit_transform(corpus: list[str]) -> list[list[int]]:
            Build the vocabulary and transform a corpus of documents into a term-document matrix.

        get_feature_names() -> list[str]:
            Get the feature names (vocabulary) as a list.
    """
    def __init__(
        self,
        lowercase: bool = True,
        separator: str = ' ',
        stop_chars: str | list[str] = '.,?!'
    ) -> None:
        """
        Initialize the CountVectorizer.

        :param lowercase: If True, convert text to lowercase (default is True).
        :param separator: The separator used to split text into words (default is a space).
        :param stop_chars: Characters to be removed from the text before processing, either as a string or a list (default is '.,?!').
        """
        self.lowercase = lowercase
        self.separator = separator
        self.vocabulary = {}
        self.stop_chars = stop_chars

    def remove_chars(self, document: str) -> str:
        """
        Remove specified characters from the given document.

        :param document: Input document.
        :return: Document with specified characters removed.
        """
        for char in self.stop_chars:
            document = document.replace(char, '')

        return document

    def split_document(self, document: str) -> list[str]:
        """
        Split a document into a list of words, with optional preprocessing.

        :param document: Input document.
        :return: List of words.
        """
        if self.lowercase:
            document = document.lower()
        document = self.remove_chars(document).strip()

        return document.split(self.separator)

    def fit(self, corpus: list[str]) -> None:
        """
        Build the vocabulary from a corpus of documents.

        :param corpus: List of documents.
        """
        for document in corpus:
            words = self.split_document(document)
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary[word] = len(self.vocabulary)

    def transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Transform a corpus of documents into a term-document matrix.

        :param corpus: List of documents.
        :return: Term-document matrix.
        """
        term_doc_matrix = [[0] * len(self.vocabulary) for _ in corpus]
        for i, document in enumerate(corpus):
            words = self.split_document(document)
            for word in words:
                if word in self.vocabulary:
                    word_index = self.vocabulary[word]
                    term_doc_matrix[i][word_index] += 1

        return term_doc_matrix

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Build the vocabulary and transform a corpus of documents into a term-document matrix.

        :param corpus: List of documents.
        :return: Term-document matrix.
        """
        self.fit(corpus)

        return self.transform(corpus)

    def get_feature_names(self) -> list[str]:
        """
        Get the feature names (vocabulary) as a list.

        :return: List of feature names.
        """
        return list(self.vocabulary)
