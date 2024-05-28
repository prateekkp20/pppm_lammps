# potential
pair_style coul/long 12.5
pair_coeff * *

# MD parameters
# kspace_style ewald 1.0e-5
kspace_style pppm 1.0e-5
kspace_modify mesh 160 160 160
kspace_modify gewald 0.2168
# kspace_modify kmax/ewald 6 6 6
neighbor 1.0 bin
# neigh_modify once yes
timestep 1.0
