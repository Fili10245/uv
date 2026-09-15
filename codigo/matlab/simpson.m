function I = simpson(f, a, b, n)
% SIMPSON  Regla de Simpson 1/3 compuesta (n par). Chapra cap. 21.
%   Uso:  I = simpson(@sin, 0, pi, 100);
    if nargin < 4, n = 100; end
    if mod(n,2) == 1, n = n + 1; end          % n debe ser par
    h = (b - a)/n;
    x = a:h:b;
    y = f(x);
    I = (h/3)*(y(1) + 4*sum(y(2:2:end-1)) + 2*sum(y(3:2:end-2)) + y(end));
end
