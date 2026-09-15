function [x, iter] = newton_sistemas(F, J, x0, tol, maxit)
% NEWTON_SISTEMAS  Newton-Raphson para sistemas no lineales. Sauer cap. 2.
%   F : handle que devuelve el vector columna F(x)
%   J : handle que devuelve la matriz jacobiana J(x)
%
%   Uso:
%     F = @(v)[v(1)^2 + v(2)^2 - 4; v(1)*v(2) - 1];
%     J = @(v)[2*v(1) 2*v(2); v(2) v(1)];
%     [x, n] = newton_sistemas(F, J, [2; 0.5], 1e-10, 50);
    x = x0(:);
    for iter = 1:maxit
        dx = -J(x)\F(x);                      % resuelve J*dx = -F
        x = x + dx;
        if norm(dx) < tol, break; end
    end
end
