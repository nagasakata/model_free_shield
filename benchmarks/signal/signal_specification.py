from benchmarks.signal.signal_arena import Obserbations

approaching_emergency_vehicle: str = f'G ({Obserbations.EMERGENCY} → (!{Obserbations.HIGHWAY} ∧ !{Obserbations.FARM}))'
not_arrowed_gg: str = f'G(!({Obserbations.HIGHWAY} ∧ {Obserbations.FARM}))'
transition_gr_rg: str = f'G(({Obserbations.HIGHWAY} ∧ !{Obserbations.FARM}) → !X(!{Obserbations.HIGHWAY} ∧ {Obserbations.FARM}))'
transition_rg_gr: str = f'G((!{Obserbations.HIGHWAY} ∧ {Obserbations.FARM}) → !X({Obserbations.HIGHWAY} ∧ !{Obserbations.FARM}))'

def safety_formula():
    return f'({approaching_emergency_vehicle} ∧ {not_arrowed_gg} ∧ {transition_gr_rg} ∧ {transition_rg_gr})'