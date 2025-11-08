# backend/apps/prestadores/mi_negocio/gestion_archivistica/storage_adapters/base.py
from abc import ABC, abstractmethod

class BaseStorageAdapter(ABC):
    """
    Define la interfaz abstracta (el "contrato") que cualquier adaptador de
    almacenamiento en la nube debe cumplir.
    """

    @abstractmethod
    def upload(self, encrypted_content: bytes, cloud_filename: str) -> str:
        """
        Sube el contenido de un archivo (ya cifrado) al proveedor de la nube.

        Args:
            encrypted_content (bytes): Los bytes del archivo ya cifrado.
            cloud_filename (str): El nombre/ruta/clave sugerida para el archivo
                                  en el almacenamiento externo.

        Returns:
            str: El identificador único (ID/clave) del archivo en el proveedor de la nube.
                 Este ID se guardará en la base de datos.
        """
        pass

    @abstractmethod
    def download(self, external_id: str) -> bytes:
        """
        Descarga un archivo desde el proveedor de la nube usando su ID externo.

        Args:
            external_id (str): El ID único del archivo que fue devuelto por el
                               método upload.

        Returns:
            bytes: El contenido cifrado del archivo tal como está almacenado.

        Raises:
            FileNotFoundError: Si el archivo con el external_id dado no se encuentra.
        """
        pass

    @abstractmethod
    def delete(self, external_id: str) -> bool:
        """
        Elimina permanentemente un archivo del proveedor de la nube.

        Args:
            external_id (str): El ID único del archivo a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        pass
