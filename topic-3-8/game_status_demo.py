"""Game Status: refactor render_status without changing its behavior."""

def recent_scores (scores):
    total = 0
    highest = scores[0]
    strong_count = 0
    for score in scores:
        total += score
        if score > highest:
            highest = score
        if score >= 80:
            strong_count += 1
        
    if total < 100:
        level = "Rookie"
    elif total < 250:
        level = "Skilled"
    else:
            level = "Expert"
            
    return total, highest, strong_count, level 
 
def format_durations (general_seconds):
    general_minutes = general_seconds // 60
    general_remainder = general_seconds % 60
    general_text = str(general_minutes) + ":"
    if general_remainder < 10:
            general_text += "0"
    general_text += str(general_remainder)
    return general_text

def make_bars(shown_type, max):
    type_filled = shown_type * 10 // max
    type_bar = "["
    for position in range(10):
        if position < type_filled:
            type_bar += "#"
        else:
            type_bar += "-"
    type_bar += "]"
    return type_bar

def clamp (vital, min, max):
    if vital < min:
         vital = min
    if vital > max:
        vital = max
    return vital

def meter_line_helper(header, valued, max, min):
    shown_type = clamp(valued, min, max)
    shown_type_bar = make_bars(shown_type, max)
    return header + " " + shown_type_bar + " " + str(shown_type) + "/" + str(max)
    
def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.


    # shown_health = clamp(health, 0, 100)
    # shown_energy = clamp(energy, 0, 60)
        # Bound the two meters.

        # Build two bars. // keeps the whole-number part of the division.
    
    # health_bar = make_bars(shown_health, 100)
    # energy_bar = make_bars(shown_energy, 60)

    # Format two durations.
    elapsed_text = format_durations(elapsed_seconds)
    best_text = format_durations(best_seconds)
   
    # Summarize the recent scores.
    total, highest, strong_count, level = recent_scores(scores)

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\nHealth  " + meter_line_helper("Health:", health, 100, 0)
    report = report + "\nEnergy  " + meter_line_helper("Energy:", energy, 60, 0)
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))

    mana = 0 
    print(meter_line_helper("Mana:", mana, 50, 0))
    
    mana = 25 
    print(meter_line_helper("Mana:", mana, 50, 0))

    mana = 50
    print(meter_line_helper("Mana:", mana, 50, 0))