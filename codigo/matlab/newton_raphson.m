function [raiz, iter] = newton_raphson(f, df, x0, tol, maxit)
% NEWTON_RAPHSON  Metodo de Newton-Raphson. Chapra cap. 6; Sauer cap. 1.
%   f, df : handles de la funcion y su derivada
%   Uso:  [r,n] = newton_raphson(@(x) x.^3-x-2, @(x) 3*x.^2-1, 1.5, 1e-8, 50);
    x = x0;
    for iter = 1:maxit
        dfx = df(x);
        if dfx == 0, error('Derivada nula; el metodo falla.'); end
        x_new = x - f(x)/dfx;
        if abs(x_new - x) < tol, x = x_new; break; end
        x = x_new;
    end
    raiz = x;
end
