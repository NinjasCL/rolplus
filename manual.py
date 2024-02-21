#!/bin/env python

import json

def translate_class(name):
    if name == "creature":
        return "Criatura"
    
    if name == "spell":
        return "Hechizo"
    
    if name == "amulet":
        return "Amuleto"
    
    if name == "power":
        return "Poder"
    
    return name.capitalize()

def magic_to_color(magic):
    if magic == "blue":
        return "is-link"
    if magic == "black":
        return "is-dark"
    if magic == "white":
        return "is-white"
    if magic == "red":
        return "is-danger"
    if magic == "green":
        return "is-success"

def translate_kind(items):
    out = ""

    for item in items:
        key = item[0]
        value = item[1]

        if key == "size":
            out += f"""
                <span class="tag is-warning">{key}: {value}</span>
            """

        elif key == "magic":
            out += f"""
                <span class="tag {magic_to_color(value)}">{key}: {value}</span>
            """
        else:
            out += f"""
                <span class="tag is-info">{key}: {value}</span>
            """

    return out

def translate_ability(items, lang = "es"):
    out = "<ul>"
    for item in items:
       for key in item.keys():
            if key == "pay" or key == "limit":
                continue

            if key == "draw_cards":
                out += f"""
                    <li>
                         <span class="spanish">Obtener <i>{item[key]}</i> carta(s).</span>
                    </li>
                    <li>
                         <span class="english hidden">Draw <i>{item[key]}</i> card(s).</span>
                    </li>
                """
                

            if lang == "en":
                if key == "inc_self_defense":
                    out += f"<li>Increment self defense by <i>{item[key]}</i> points.</li>"

                if key == "inc_self_attack":
                    out += f"<li>Increment self attack by <i>{item[key]}</i> points.</li>"

                if key == "block_spin_opponent_power":
                    out += f"<li>Block activation of <i>{item[key]}</i> powers.</li>"

                if key == "block_spin_opponent_creature":
                    out += f"<li>Block activation of <i>{item[key]}</i> creatures.</li>"
                
                if key == "inc_holder_defense":
                    out += f"<li>Gives holder <i>{item[key]}</i> defense points.</li>"
                
                if key == "dec_opponent_life":
                    out += f"<li>Damages opponent's life by <i>{item[key]}</i> points.</li>"
                
                if key == "inc_owner_life":
                    out += f"<li>Restores player life by <i>{item[key]}</i> points.</li>"
                
                if key == "alter_owner_field":
                    element = item[key]
                    command = element["do"]
                    
                    if command == "inc_defense_in_all_creatures":
                        quantity = element["quantity"]
                        out += f"<li>Increase defense in all player field creatures by <i>{quantity}</i> points.</li>"
                    
                    if command == "inc_attack_in_all_creatures":
                        quantity = element["quantity"]
                        out += f"<li>Increase attack in all player field creatures by <i>{quantity}</i> points.</li>"
                    
                    if command == "set_shield_to_all_creatures":
                        quantity = element.get("quantity")  or element.get("quantiy") or 1
                        defense = element.get("inc_defense")
                        if defense:
                            out += f"<li>All player field creatures are <i>defenders</i> for the next <i>{quantity}</i> turns with {defense} additional defense points.</li>"
                        else:    
                            out += f"<li>All player field creatures are <i>defenders</i> for the next <i>{quantity}</i> turns.</li>"

                if key == "alter_opponent_field":
                    element = item[key]
                    command = element["do"]

                    if command == "delete_mystic_status_from_all_creatures":
                        out += f"<li>Erase <i>Mystic</i> status from opponent's field creatures.</li>"
                    
                    if command == "destroy":
                        quantity = element.get("quantity") or 1
                        type = element.get("type").capitalize()
                        
                        out += f"<li>Destroys <i>{quantity}</i> <i>{type}</i> cards from opponent's field.</li>"
                    


            if lang == "es":
                if key == "inc_self_defense":
                    out += f"<li>Aumenta la propia defensa por <i>{item[key]}</i> puntos.</li>"

                if key == "inc_self_attack":
                    out += f"<li>Aumenta el propio ataque por <i>{item[key]}</i> puntos.</li>"

                if key == "block_spin_opponent_power":
                    out += f"<li>Bloquea activar <i>{item[key]}</i> poderes.</li>"

                if key == "block_spin_opponent_creature":
                    out += f"<li>Bloquea activar <i>{item[key]}</i> criaturas.</li>"
                
                if key == "inc_holder_defense":
                    out += f"<li>Da al portador <i>{item[key]}</i> puntos de defensa.</li>"
                
                if key == "dec_opponent_life":
                    out += f"<li>Daña la vida del adversario en <i>{item[key]}</i> puntos.</li>"
                
                if key == "inc_owner_life":
                    out += f"<li>Restaura la vida del aprendiz en <i>{item[key]}</i> puntos.</li>"
                
                if key == "alter_owner_field":
                    element = item[key]
                    command = element["do"]

                    if command == "inc_defense_in_all_creatures":
                        quantity = element["quantity"]
                        out += f"<li>Aumenta la defensa de todas las criaturas del campo del aprendiz en <i>{quantity}</i> puntos.</li>"

                    if command == "inc_attack_in_all_creatures":
                        quantity = element["quantity"]
                        out += f"<li>Aumenta el ataque de todas las criaturas del campo del aprendiz en <i>{quantity}</i> puntos.</li>"

                    if command == "set_shield_to_all_creatures":
                        quantity = element.get("quantity") or 1
                        defense = element.get("inc_defense")
                        if defense:
                            out += f"<li>Las criaturas del campo del jugador serán <i>defensoras</i> por los siguientes <i>{quantity}</i> turnos con {defense} puntos de defensa adicional.</li>"
                        else:    
                            out += f"<li>Las criaturas del campo del jugador serán <i>defensoras</i> por los siguientes <i>{quantity}</i> turnos.</li>"

                if key == "alter_opponent_field":
                    element = item[key]
                    command = element.get("do")

                    if command == "delete_mystic_status_from_all_creatures":
                        out += f"<li>Elimina el estado <i>Místico</i> de las criaturas del oponente en el campo.</li>"
                    
                    if command == "destroy":
                        quantity = element.get("quantity") or 1
                        type = element.get("type")

                        if type == "amulet":
                            type = "Amuleto"
                        if type == "power":
                            type = "Poder"
                        if type == "creature":
                            type = "Criatura"
                        if type == "spell":
                            type = "Hechizo"
                        
                        out += f"<li>Destruye <i>{quantity}</i> cartas del tipo <i>{type}</i> del oponente en el campo.</li>"
                    

    
    out += "</ul>"

    return out

def calculate_total_pay(items):
    total = 0
    for item in items:
        total += item["pay"]

    return total

def calculate_total_turns(items, lang = "es"):
    turns = -1
    for item in items:
        if item["limit"] > turns:
            turns = item["limit"]
    
    if turns < 0:
        turns = "Ilimitado"
        if lang == "en":
            turns = "Unlimited"

    return turns


def special_fields(card, lang = "es"):
    abilities = card.get("abilities")
    out = ""
    if abilities and abilities.get("special"):
        out += """
            <tr>
                <td>
                    <span class="spanish">Especial</span><span class="english hidden">Special</span>
                </td>
                <td>
    
        """
        special = abilities.get("special")
        for item in special:
            for key in item.keys():
                if key == "can_defend_multiple_times":
                    out += f"""
                    <span class="spanish">Puede defender hasta {item[key]} veces.</span>
                    <span class="english hidden">Can defend up to {item[key]} times.</span>
                    """
                if key == "can_attack_multiple_times":
                    out += f"""
                    <span class="spanish">Puede atacar hasta {item[key]} veces.</span>
                    <span class="english hidden">Can attack up to {item[key]} times.</span>
                    """
        out += """
            </td>
        </tr>
        """


    return out


def show_creature_fields(card):
    
    if card["class"] == "creature": 
        return f"""
            <tr>
                <td>
                    <span class="spanish">Ataque</span><span class="english hidden">Attack</span>
                </td>
                <td>
                    {card["attack"]}
                </td>
            </tr>
            <tr>
                <td>
                    <span class="spanish">Defensa</span><span class="english hidden">Defense</span>
                </td>
                <td>
                    {card["defense"]}
                </td>
            </tr>
            <tr>
                <td>
                    <span class="spanish">Tipo</span><span class="english hidden">Type</span>
                </td>
                <td>
                    {card["type"].capitalize()}
                </td>
            </tr>
            <tr>
                <td>
                    <span class="spanish">Subtipo</span><span class="english hidden">Subtype</span>
                </td>
                <td>
                    {card["subtype"].capitalize()}
                </td>
            </tr>
            {special_fields(card)}
            
        """
    else:
        return ""
    
def translate_abilities(abilities, lang = "es"):
    out = ""

    if len(abilities) <= 0 or len(abilities["main"]) <= 0:
        if lang == "en":
            return "None"
        return "Ninguna"

    main = abilities["main"]
    main_pay = calculate_total_pay(main)
    main_turns = calculate_total_turns(main, lang)

    if lang == "en":
        out += f"""
        <h3>Pay: {main_pay}</h3>
        <h3>Turns: {main_turns}</h3>
        {translate_ability(main, lang)}
        """

    if lang == "es":
        out += f"""
        <h3>Pagar: {main_pay}</h3>
        <h3>Turnos: {main_turns}</h3>
        {translate_ability(main, lang)}
        """



    return out

def show_before_activate_fields(card):
    abilities = card.get("abilities").get("on_activate") or []
    out = ""
    for item in abilities:
        out += """
            <tr>
                <td>
                    <span class="spanish">Efectos al Activar</span><span class="english hidden">Activation Effects</span>
                </td>
        """
        for key in item.keys():
            if key == "inc_owner_power":
                out += f"""
                    <td>
                         <span class="spanish">Obtener <i>{item[key]}</i> poder(es).</span>
                         <span class="english hidden">Obtain <i>{item[key]}</i> power(s).</span>
                    </td>
                """

            if key == "draw_cards":
                out += f"""
                
                    <td>
                         <span class="spanish">Obtener <i>{item[key]}</i> carta(s).</span>
                         <span class="english hidden">Draw <i>{item[key]}</i> card(s).</span>
                    </td>
                
                """

        out += "</tr>"
    
    return out

def show_before_attack_fields(card):
    abilities = card.get("abilities").get("on_before_attack") or []
    out = ""
    for item in abilities:
        out += """
            <tr>
                <td>
                    <span class="spanish">Efectos al Atacar</span><span class="english hidden">Attack Effects</span>
                </td>
        """
        for key in item.keys():
            if key == "dec_owner_life":
                out += f"""
                    <td>
                         <span class="spanish">Reduce <i>{item[key]}</i> punto de vida al aprendiz (aumenta con la defensa).</span>
                         <span class="english hidden">Decrease <i>{item[key]}</i> player's life points (increase with defense).</span>
                    </td>
                """
    
    return out

def show_before_cast_fields(card):
    abilities = card.get("abilities").get("on_before_cast") or []
    out = ""
    for item in abilities:
        out += """
            <tr>
                <td>
                    <span class="spanish">Efectos al Invocar</span><span class="english hidden">Invocation Effects</span>
                </td>
        """
        for key in item.keys():
            if key == "draw_cards":
                out += f"""
                
                    <td>
                         <span class="spanish">Obtener <i>{item[key]}</i> carta(s).</span>
                         <span class="english hidden">Draw <i>{item[key]}</i> card(s).</span>
                    </td>
                
                """
            if key == "dec_opponent_life":
                out += f"""
                    <td>
                         <span class="spanish">Disminuye <i>{item[key]}</i> puntos de vida al oponente.</span>
                         <span class="english hidden">Drains <i>{item[key]}</i> opponent's life points.</span>
                    </td>
                """
            
            if key == "inc_owner_life":
                out += f"""
                    <td>
                         <span class="spanish">Aumenta <i>{item[key]}</i> puntos de vida al aprendiz.</span>
                         <span class="english hidden">Recovers <i>{item[key]}</i> player life points.</span>
                    </td>
                """
            
            if key == "block_spin_opponent_creature":
                out += f"""
                    <td>
                         <span class="spanish">Bloquea activar <i>{item[key]}</i> criaturas del oponente por 1 turno.</span>
                         <span class="english hidden">Blocks the activation of <i>{item[key]}</i> opponent's creatures by 1 turn.</span>
                    </td>
                """

            if key == "owner_min_activated_creatures":
                out += f"""
                    <td>
                         <span class="spanish">Requiere <i>{item[key]}</i> criaturas que se hayan activado durante la partida.</span>
                         <span class="english hidden">Requires <i>{item[key]}</i> activated creatures during the match.</span>
                    </td>
                """

            if key == "alter_opponent_field":
                element = item[key]
                command = element.get("do")
                if command == "destroy":
                    quantity = element.get("quantity") or element.get("quantiy") or 1
                    type = element.get("type")


                    out += f"""
                    <td>
                         <span class="spanish">Destruye {quantity} {translate_class(type)}(s).</span>
                         <span class="english hidden">Destroys {quantity} {type.capitalize()}</span>
                    </td>
                    """
                
        

        out += "</tr>"
    
    return out


# TODO: Check why None appears in spells

def main():
    data = open("./cards.json", encoding="utf8").read()
    cards = json.loads(data)

    template = open("./template.html", encoding="utf8").read()

    cards_table = ""

    for card in cards:
        # Omit disabled cards
        settings = card["settings"]
        if len(settings) > 0:
            disabled_setting = settings[0]
            if disabled_setting["disabled"] == True:
                continue

        cards_table += f"""
        
        <label class="table-header">
            #{card["id"]} <span class="spanish">{card["name"]["spanish"]}</span><span class="english hidden">{card["name"]["english"]}</span>
            <img src="cards/{card["id"]}.jpg" class="image">
            <table>
            <tbody>
                <tr>
                    <td>
                        <span class="spanish">Clase</span><span class="english hidden">Class</span>
                    </td>
                    <td>
                        <span class="spanish">{translate_class(card["class"])}</span><span class="english hidden">{card["class"].capitalize()}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="spanish">Nivel</span><span class="english hidden">Level</span>
                    </td>
                    <td>
                        {card["level"]}
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="spanish">Rareza</span><span class="english hidden">Rarity</span>
                    </td>
                    <td>
                        {card["rarity"]["value"].capitalize()} ({0.1 if (100 - card["rarity"]["percent"] <= 0) else 100 - card["rarity"]["percent"]}%)
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="spanish">Costo</span><span class="english hidden">Cost</span>
                    </td>
                    <td>
                        {card["casting_cost"]}
                    </td>
                </tr>
                
                {show_creature_fields(card)}
                {show_before_cast_fields(card)}
                {show_before_activate_fields(card)}
                {show_before_attack_fields(card)}
                <tr>
                    <td>
                        <span class="spanish">Copias por Mazo</span><span class="english hidden">Max Per Deck</span>
                    </td>
                    <td>
                        {card["max_per_deck"]}
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="spanish">Especie</span><span class="english hidden">Kind</span>
                    </td>
                    <td>
                        <span class="spanish">{translate_kind(card["kind"])}</span><span class="english hidden">{translate_kind(card["kind"])}</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <span class="spanish">Habilidades</span><span class="english hidden">Abilities</span>
                    </td>
                    <td>
                        <span class="spanish">{translate_abilities(card["abilities"])}</span><span class="english hidden">{translate_abilities(card["abilities"], "en")}</span>
                    </td>
                </tr>
            </tbody>
        </table>
        
        </label>
        """

    output = template.replace("{cards}", cards_table)

    with open("./manual.html", "w", encoding="utf-8") as manual:
        manual.write(output)

if __name__ == "__main__":
    main()