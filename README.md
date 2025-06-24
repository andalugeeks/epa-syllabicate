# EPA Syllabifier

Módulo Python para la silabificación de palabras.

## Uso

```python
from epa_syllabifier import syllabify

# Ejemplo de uso
word = "ejemplo"
syllables = syllabify(word)
print(syllables)  # ['e', 'jem', 'plo']
```

## Desarrollo

### Instalación para desarrollo

Para contribuir al proyecto, primero clona el repositorio y luego instala las dependencias de desarrollo:

```bash
git clone https://github.com/andalugeeks/epa-syllabifier.git
cd epa-syllabifier
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

### Ejecución de tests

Para ejecutar los tests:

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con cobertura
pytest --cov=epa_syllabifier
```

## Requisitos

- Python >= 3.8

## Licencia

Este proyecto está licenciado bajo la Licencia GPL v3 - ver el archivo [LICENSE](LICENSE) para más detalles. 