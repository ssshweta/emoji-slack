# emoji-slack
like the csh one but just a python script

# example
Two outputs occur with every input.
1. **Emoji String** returns an aliasing with every single letter with a slack emoji.
2. **Emoji-word/phrase Replacements** replace every _phrase_ or individual word with its equivalent emoji, if specified.

### Example Usage:
```bash
> emoji-slack$ python3 espell.py
Enter message: I guess they don't have an intuit branch in alabama because they aren't really into it.

Emoji String:
:i::blank::google::magnet::nodejs::heavy_dollar_sign::sublime::blank::t_scrabble::h_scrabble::e::byu::blank::duo::o2::northeastern:':t_zucchini::blank::h_scrabble::amplitude::vim::ie::blank::afc::netscape::blank::i_scrabble::netscape::t_bubble::magnet::i::tesla-motors::blank::b_scrabble::r_scrabble::afc::n_scrabble::bears::h_scrabble::blank::care_info::netflix::blank::a_scrabble::loss::appdynamics::bengals::angels::maccas::uofa::blank::b::nodejs::coinbase::amplitude::usertestingdotcom::heavy_dollar_sign::e::blank::t_zucchini::astros::e::y_scrabble::blank::apollo::rust::e::netscape:':titan::blank::r_scrabble::e::a::muscle::skin-tone-2::muscle::y_scrabble::blank::i_scrabble::netflix::tesla-motors::o::blank::care_info::t_zucchini:.

Emoji-word Replacement Strings:
i guess they don't have an :intuit: branch in :alabama: because they aren't really :intuit:.
> emoji-slack$
```

### How it looks like:
Emoji String:
![Emoji String](examplestring.jpeg)

Emoji-word Replacement Strings:
![Emoji Replacement](examplereplacement.jpeg)
