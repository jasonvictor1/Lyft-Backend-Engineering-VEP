class Serviceable:
    def needs_service(self) -> bool:
        """Determine if the object needs service."""
        raise NotImplementedError("The method needs_service should be implemented by subclasses.")
