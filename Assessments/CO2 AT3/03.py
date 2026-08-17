import re
import nltk

from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download("wordnet")
nltk.download("omw-1.4")

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

documents = [
    "organization organizes technology products",
    "organizer organizes business events",
    "technology companies develop software",
    "business organizations manage products",
    "developers organize technology projects",
    "companies are organizing new software"
]

labels = [
    "technology",
    "business",
    "technology",
    "business",
    "technology",
    "technology"
]


def no_stemming(text):
    return text.lower()


def stemming(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return " ".join(ps.stem(word) for word in words)


def lemmatization(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return " ".join(lemmatizer.lemmatize(word) for word in words)


methods = {
    "Without Stemming": no_stemming,
    "Porter Stemming": stemming,
    "Lemmatization": lemmatization
}


for name, function in methods.items():

    processed = [function(doc) for doc in documents]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(processed)

    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.3, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print("\n", name)
    print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
    print("Accuracy:", round(accuracy * 100, 2), "%")