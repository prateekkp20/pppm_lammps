# potential
pair_style coul/long 12.5
pair_coeff * *

# MD parameters
kspace_style ewald 1.0e-5
kspace_modify slab 3
kspace_modify mesh 60 60 60
kspace_modify gewald 0.2168
# kspace_modify kmax/ewald 6 6 6
neighbor 1.0 bin
# neigh_modify once yes
neigh_modify one 10000
timestep 1.0
