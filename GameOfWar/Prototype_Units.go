package main

import (
	"fmt"
)

type Uniter interface {
	Move()
	Attack()
	Die()
	Check()
	Seek()
	Error()
}

type WarUnits struct {
	name string
}

type Soldiers struct {
	WarUnits
	life     int
	damage   int
	unitType string
}

func (x Soldiers) Move() {
	fmt.Println(x.name, " is moving")
}

func (x Soldiers) Attack() {
	fmt.Println("Soldier attack ", x.damage)
}

func (x Soldiers) Die() {
	if x.life > 0 {
		fmt.Println("Soldier is alive")
	} else {
		fmt.Println("Soldier is dead")
	}
}

func (x Soldiers) Check() {
	fmt.Println("Unit its type: ", x.unitType)
}

func (x Soldiers) Seek() {
	fmt.Println("Soldier is seeking")
}

func (x Soldiers) Error() {
	fmt.Println("Invalid query")
}

func main() {
	m := map[string]Uniter{
		"unit1": Soldiers{WarUnits{"Jonh"}, 100, 10, "Soldier"},
		"unit2": Soldiers{WarUnits{"Doe"}, 100, 10, "Soldier"},
		"unit3": Soldiers{WarUnits{"PanzerSmith"}, 400, 20, "Tank"},
		"unit4": Soldiers{WarUnits{"PumKaboom"}, 200, 50, "Bomber"},
		"unit5": Soldiers{WarUnits{"DeadEye"}, 100, 30, "Sniper"},
	}
	for i := 0; i < 3; i++ {
		fmt.Println("Enter Soldier and query (seek, life, check, move, attack)")
		fmt.Print(">")
		var unit, op string
		fmt.Scan(&unit, &op)
		if op == "seek" {
			m[unit].Seek()
		} else if op == "life" {
			m[unit].Die()
		} else if op == "check" {
			m[unit].Check()
		} else if op == "move" {
			m[unit].Move()
		} else if op == "attack" {
			m[unit].Attack()
		} else {
			m[unit].Error()
		}
	}
}
