class ExperimentCatalog:
    """
    Acts as a categorizable metadata catalog for scientific experiments and standard protocol designs.
    """
    def __init__(self):
        self.catalog = {}

    def register_template(self, category: str, template_name: str, template_dict: dict):
        if category not in self.catalog:
            self.catalog[category] = {}
        self.catalog[category][template_name] = template_dict

    def get_template(self, category: str, template_name: str) -> dict:
        return self.catalog.get(category, {}).get(template_name)

    def list_templates(self) -> dict:
        return self.catalog
