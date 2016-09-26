function [ score ] = MATLAB_bowler( game )
%BOWLING_SCORE:  Function to calculate bowling scores given game = string
    %  game example = 'XXXXXXXXXXXX' (see bowling_score_tester.m)

game(game=='-') = '0';
frame_scores = zeros(1,10);

%% LAST FRAME Scoring: counts bonus frames and scores final frame
nrolls = length(game);
strike_index = find(game=='X');
bonus_counter = nrolls + length(strike_index);

counter = 0; % Invalid Games are set to zero

if bonus_counter == 20
    frame_scores(end) = str2double( game(end-1)) +str2double(game(end));
    counter = length(game)-2;
elseif bonus_counter == 21
    frame_scores(end)  = 10 + str2double(game(end-2));
    counter = length(game)- 3;
elseif bonus_counter == 22
    if game(nrolls) == 'X' || game(nrolls) == '/'
        frame_scores(end) = 20;
    else
        frame_scores(end) = 10 +str2double( game(end-1)) +str2double(game(end));
    end
    counter = length(game)- 3;
elseif bonus_counter == 23
    frame_scores(end) = 20 + str2double(game(end));
    counter = length(game)- 3;
elseif bonus_counter == 24
    frame_scores(end) = 30;
    counter = length(game)- 3;
else
end
%% Using last frame score, continue filling in frame scores backwards:
frame = 9;

while counter ~= 0
    if game(counter) == 'X' % Check for strike
        if game(counter+1)== 'X' % is followed by another strike?
            if game(counter+2)== 'X' % Turkey
                frame_scores(frame) = 30;
            else
                frame_scores(frame) = 20 + str2double(game(counter +2));
            end
        elseif game(counter+2) == '/' % if strike followed by a spare
            frame_scores(frame) = 20;
        else
            frame_scores(frame) = 10 + frame_scores(frame+1);
        end
        counter = counter - 1;
        frame = frame - 1;
    elseif game(counter) == '/'
        if game(counter+1)== 'X' % if spare followed by a strike
            frame_scores(frame) = 20;
        else
            frame_scores(frame) = 10 + str2double(game(counter+1));
        end
        counter = counter - 2;
        frame = frame - 1;
    else
        frame_scores(frame) = str2double(game(counter)) + str2double(game(counter-1));
        counter = counter - 2;
        frame = frame - 1;
    end
end
score = sum(frame_scores);
end
