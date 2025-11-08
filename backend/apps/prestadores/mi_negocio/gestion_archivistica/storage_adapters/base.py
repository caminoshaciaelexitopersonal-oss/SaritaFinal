from abc import ABC, abstractmethod

class BaseStorageAdapter(ABC):
    """
    Define la interfaz abstracta (el "contrato") que cualquier adaptador de
    almacenamiento debe cumplir.

    Esta clase no se puede instanciar directamente. Su propósito es garantizar
    que todos los adaptadores (S3, Google Drive, etc.) tengan una funcionalidad
    consistente y predecible.
    """

    @abstractmethod
    def upload(self, encrypted_content: bytes, cloud_filename: str) -> str:
        """
        Sube el contenido de un archivo (ya cifrado) al proveedor de almacenamiento.

        Args:
            encrypted_content (bytes): Los bytes del archivo ya cifrado.
            cloud_filename (str): El nombre/ruta sugerida para el archivo.

        Returns:
            str: El identificador único (ID/clave) del archivo en el proveedor.
        """
        pass

    @abstractmethod
    def download(self, external_id: str) -> bytes:
        """
        Descarga un archivo desde el proveedor usando su ID externo.

        Args:
            external_id (str): El ID único del archivo.

        Returns:
            bytes: El contenido cifrado del archivo.

        Raises:
            FileNotFoundError: Si el archivo no se encuentra.
        """
        pass

    @abstractmethod
    def delete(self, external_id: str) -> bool:
        """
        Elimina permanentemente un archivo del proveedor.

        Args:
            external_id (str): El ID único del archivo a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        pass
