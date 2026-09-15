function [raiz, iter] = falsa_posicion(f, a, b, tol, maxit)
% FALSA_POSICION  Metodo de la falsa posicion (regula falsi). Chapra cap. 5.
%   Uso:  [r, n] = falsa_posicion(@(x) x.^3 - x - 2, 1, 2, 1e-6, 100);
    if f(a)*f(b) > 0
        error('No hay cambio de signo en [a,b].');
    end
    c = a;
    for iter = 1:maxit
        c_old = c;
        c = (a*f(b) - b*f(a))/(f(b) - f(a));    % interseccion con el eje x
        if f(c) == 0, break; end
        if iter > 1 && abs((c - c_old)/c) < tol, break; end
        if f(a)*f(c) < 0, b = c; else, a = c; end
    end
    raiz = c;
end
