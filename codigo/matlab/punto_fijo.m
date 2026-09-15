function [raiz, iter] = punto_fijo(g, x0, tol, maxit)
% PUNTO_FIJO  Iteracion de punto fijo x = g(x). Chapra cap. 6.
%   Uso:  [r, n] = punto_fijo(@(x) cos(x), 0.5, 1e-6, 100);
    x = x0;
    for iter = 1:maxit
        x_new = g(x);
        if abs(x_new - x) < tol, x = x_new; break; end
        x = x_new;
    end
    raiz = x;
end
