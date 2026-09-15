function I = trapecio(f, a, b, n)
% TRAPECIO  Regla del trapecio compuesta. Chapra cap. 21.
%   Uso:  I = trapecio(@sin, 0, pi, 1000);
    if nargin < 4, n = 100; end
    h = (b - a)/n;
    x = a:h:b;
    y = f(x);
    I = h*(0.5*y(1) + sum(y(2:end-1)) + 0.5*y(end));
end
