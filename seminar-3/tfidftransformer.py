import math


class TfidfTransformer:
    """
    Transform a term-document matrix into a TF-IDF matrix.

    Methods:
        idf_transform(count_matrix: List[List[int]]) -> List[float]:
            Calculate the Inverse Document Frequency (IDF) values for
                the given term-document matrix.

        tf_transform(count_matrix: List[List[int]]) -> List[List[float]]:
            Calculate the Term Frequency (TF) values for the
                given term-document matrix.

        fit_transform(count_matrix: List[List[int]]) -> List[List[float]]:
            Transform a term-document matrix into a TF-IDF matrix.
    """
    def idf_transform(self, count_matrix: list[list[int]]) -> list[float]:
        """
        Calculate the Inverse Document Frequency (IDF) values for the
            given term-document matrix.

        :param count_matrix: Term-document matrix as a list of lists.
        :return: List of IDF values.
        """
        idf_matrix = [None] * len(count_matrix[0])
        doc_count = len(count_matrix)
        for i, *word_count in zip(range(len(count_matrix[0])), *count_matrix):
            df = sum((c for c in word_count if c > 0))
            idf_matrix[i] = math.log((doc_count + 1) / (df + 1)) + 1

        return idf_matrix

    def tf_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Calculate the Term Frequency (TF) values for the
            given term-document matrix.

        :param count_matrix: Term-document matrix as a list of lists.
        :return: List of TF values as a term-document matrix.
        """
        tf_matrix = [None] * len(count_matrix)
        for i in range(len(count_matrix)):
            total = sum(count_matrix[i])
            tf_matrix[i] = [j / total for j in count_matrix[i]]

        return tf_matrix

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Transform a term-document matrix into a TF-IDF matrix.

        :param count_matrix: Term-document matrix as a list of lists.
        :return: List of TF-IDF values as a term-document matrix.
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tfidf_matrix = [None] * len(count_matrix)
        for i, row in enumerate(tf_matrix):
            tfidf_matrix[i] = [tf * idf for tf, idf in zip(row, idf_matrix)]

        return tfidf_matrix
