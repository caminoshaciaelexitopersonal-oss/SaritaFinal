class LanguageDiversityValidator:
    """
    Verifies the presence of required diverse languages in the verifier set.
    """
    REQUIRED_LANGUAGES = {"Python", "Go", "JavaScript"}

    @staticmethod
    def validate_diversity(provenances: list):
        found_languages = set(p["language"] for p in provenances)
        intersect = found_languages.intersection(LanguageDiversityValidator.REQUIRED_LANGUAGES)

        return len(intersect) >= 2, f"Languages found: {found_languages}"
