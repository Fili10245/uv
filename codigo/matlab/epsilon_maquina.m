% epsilon_maquina.m -- Epsilon de maquina y errores de redondeo. Chapra cap. 3.
% Script: ejecutar directamente en MATLAB u Octave.

eps_calc = 1;
while (1 + eps_calc) > 1
    eps_calc = eps_calc / 2;
end
eps_calc = eps_calc * 2;          % ultimo valor que aun afecta a la suma

fprintf('Epsilon de maquina calculado: %.3e\n', eps_calc);
fprintf('eps() de MATLAB:              %.3e\n', eps);
fprintf('0.1 + 0.2 == 0.3 ? %d\n', (0.1 + 0.2) == 0.3);
fprintf('0.1 + 0.2 = %.17f\n', 0.1 + 0.2);
