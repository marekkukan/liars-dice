#!/usr/bin/env julia

while !eof(STDIN)
    line = readline()
    parts = split(line)
    if parts[1] == "NEW_ROUND"
        quantity, value = 0, 6
    elseif parts[1] == "PLAYER_BIDS"
        quantity, value = parse(Int, parts[3]), parse(Int, parts[4])
    elseif parts[1] == "PLAY"
        if quantity > 0 && rand() < 0.4
            println("CHALLENGE")
        else
            println("BID $(quantity + 1) $(value)")
        end
    end
end
