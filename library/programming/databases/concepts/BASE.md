# BASE - (Basically Available, Soft state, Eventual consistency)
- Basically Available: Instead of immediate consistency, BASE-modelled databases 
  will ensure the availability of data by spreading and replicating it across the 
  nodes of the database cluster.
- Soft State: Due to the lack of immediate consistency, the data values may change 
  over time. The BASE model breaks off with the concept of a database that 
  obligates its own consistency, delegating that responsibility to developers.
- Eventually Consistent: BASE does not obligates immediate consistency but it does 
  not mean that it never achieves it. However, until it does, the data reads are 
  still possible (even though they might not reflect reality).

## ACID vs BASE:
- The ACID model provides a consistent system.
- The BASE model provides high availability.
