% MULTIPLICIDAD_CSTR  Estados estacionarios múltiples en un CSTR adiabático
% (Fogler, cap. 12). Reacción A -> B de primer orden, irreversible, fase líquida.
%
% Los estados estacionarios son las intersecciones de:
%   G(T) = (-dH) * X_MB(T)     calor generado
%   R(T) = Cp * (T - T0)       calor removido (adiabático)

% ---- Datos ----
T0  = 320;      % K, temperatura de alimentación
tau = 10;       % min, tiempo espacial
k1  = 0.002;    % 1/min, constante de velocidad a T1
T1  = 350;      % K
EoR = 10000;    % K, energía de activación / R
dH  = -8000;    % cal/mol, calor de reacción
Cp  = 40;       % cal/(mol K), suma de Theta_i * Cp_i

k = @(T) k1*exp(EoR*(1/T1 - 1./T));
X = @(T) tau*k(T)./(1 + tau*k(T));     % balance de moles (CSTR)
G = @(T) -dH*X(T);                     % calor generado
R = @(T) Cp*(T - T0);                  % calor removido
f = @(T) G(T) - R(T);

% ---- Buscar intersecciones G(T) = R(T) ----
T = linspace(T0, 560, 2000);
y = f(T);
fprintf('Estados estacionarios:\n');
for i = 1:numel(T)-1
    if y(i)*y(i+1) < 0
        Ts = fzero(f, [T(i) T(i+1)]);
        % Si G - R pasa de + a -, la pendiente de R supera a la de G: estable
        if y(i) > 0, tipo = 'estable'; else, tipo = 'inestable'; end
        fprintf('  T = %6.1f K   X = %.3f   (%s)\n', Ts, X(Ts), tipo);
    end
end

% ---- Gráfica ----
plot(T, G(T), 'r', T, R(T), 'b'); grid on
xlabel('T [K]'); ylabel('cal/mol');
title('Multiplicidad de estados estacionarios en un CSTR');
legend('G(T) generado', 'R(T) removido', 'Location', 'northwest');
