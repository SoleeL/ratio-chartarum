# application/ports/random_port.py

from typing import Protocol, Sequence, TypeVar

T = TypeVar("T")


class RandomPort(Protocol):
    """
    Puerto de salida para generación de valores aleatorios.
    Permite desacoplar el dominio de la librería random concreta.
    """

    def choice(self, items: Sequence[T]) -> T:
        """Devuelve un elemento aleatorio de la secuencia."""
        ...

    def randint(self, a: int, b: int) -> int:
        """Devuelve un entero aleatorio en el rango [a, b]."""
        ...

    def random(self) -> float:
        """Devuelve un float aleatorio en el rango [0.0, 1.0)."""
        ...