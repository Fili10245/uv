function [raiz, iter] = biseccion(f, a, b, tol, maxit)
% BISECCION  Raiz de f en [a,b] por biseccion. Chapra cap. 5; Sauer cap. 1.
%   f     : handle, p. ej. @(x) x.^3 - x - 2
%   a, b  : extremos con f(a)*f(b) < 0
%   tol   : tolerancia sobre el ancho del intervalo
%   maxit : maximo de iteraciones
%
%   Uso:  [r, n] = biseccion(@(x) x.^3 - x - 2, 1, 2, 1e-6, 100);
    if f(a)*f(b) > 0
        error('No hay cambio de signo en [a,b].');
    end
    iter = 0;
    while (b - a)/2 > tol && iter < maxit
        c = (a + b)/2;                 % punto medio
        if f(c) == 0, break; end
        if f(a)*f(c) < 0
            b = c;                     % la raiz esta en [a,c]
        else
            a = c;                     % la raiz esta en [c,b]
        end
        iter = iter + 1;
    end
    raiz = (a + b)/2;
end
