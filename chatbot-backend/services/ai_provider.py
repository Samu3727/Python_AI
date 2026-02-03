from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Interfaz abstracta para proveedores de IA.
    Implementa el principio Open/Closed: abierto para extensión, cerrado para modificación.
    """
    
    @abstractmethod
    async def get_response(self, message: str) -> str:
        """
        Obtiene una respuesta del proveedor de IA.
        
        Args:
            message: El mensaje del usuario
            
        Returns:
            La respuesta generada por la IA
            
        Raises:
            Exception: Si hay un error al obtener la respuesta
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """
        Verifica si el proveedor está disponible y configurado correctamente.
        
        Returns:
            True si el proveedor está disponible, False en caso contrario
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """
        Obtiene el nombre del proveedor.
        
        Returns:
            Nombre del proveedor
        """
        pass
