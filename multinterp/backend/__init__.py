from multinterp.backend._scipy import scipy_multinterp
from multinterp.backend._cupy import cupy_multinterp
from multinterp.backend._numba import numba_multinterp
from multinterp.backend._jax import jax_multinterp

backend_functions = {
    "scipy": scipy_multinterp,
    "numba": numba_multinterp,
    "cupy": cupy_multinterp,
    "jax": jax_multinterp,
}


def multinterp(grids, values, args, backend="numba"):
    if backend in backend_functions:
        return backend_functions[backend](grids, values, args)
    else:
        raise ValueError(f"Invalid backend: {backend}")
