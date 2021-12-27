namespace Namespace {
    
    using os;
    
    using re;
    
    using math;
    
    using @string;
    
    using codecs;
    
    using json;
    
    using product = itertools.product;
    
    using getsourcefile = inspect.getsourcefile;
    
    using open = io.open;
    
    using System.Collections.Generic;
    
    using System.Linq;
    
    using System;
    
    using tokenize = nltk.tokenize;
    
    using requests;
    
    public static class Module {
        
        static Module() {
            @"
If you use the VADER sentiment analysis tools, please cite:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
";
        }
        
        public static object B_INCR = 0.293;
        
        public static object B_DECR = -0.293;
        
        public static object C_INCR = 0.733;
        
        public static object N_SCALAR = -0.74;
        
        public static object NEGATE = new List<object> {
            "aint",
            "arent",
            "cannot",
            "cant",
            "couldnt",
            "darent",
            "didnt",
            "doesnt",
            "ain't",
            "aren't",
            "can't",
            "couldn't",
            "daren't",
            "didn't",
            "doesn't",
            "dont",
            "hadnt",
            "hasnt",
            "havent",
            "isnt",
            "mightnt",
            "mustnt",
            "neither",
            "don't",
            "hadn't",
            "hasn't",
            "haven't",
            "isn't",
            "mightn't",
            "mustn't",
            "neednt",
            "needn't",
            "never",
            "none",
            "nope",
            "nor",
            "not",
            "nothing",
            "nowhere",
            "oughtnt",
            "shant",
            "shouldnt",
            "uhuh",
            "wasnt",
            "werent",
            "oughtn't",
            "shan't",
            "shouldn't",
            "uh-uh",
            "wasn't",
            "weren't",
            "without",
            "wont",
            "wouldnt",
            "won't",
            "wouldn't",
            "rarely",
            "seldom",
            "despite"
        };
        
        public static object BOOSTER_DICT = new Dictionary<object, object> {
            {
                "absolutely",
                B_INCR},
            {
                "amazingly",
                B_INCR},
            {
                "awfully",
                B_INCR},
            {
                "completely",
                B_INCR},
            {
                "considerable",
                B_INCR},
            {
                "considerably",
                B_INCR},
            {
                "decidedly",
                B_INCR},
            {
                "deeply",
                B_INCR},
            {
                "effing",
                B_INCR},
            {
                "enormous",
                B_INCR},
            {
                "enormously",
                B_INCR},
            {
                "entirely",
                B_INCR},
            {
                "especially",
                B_INCR},
            {
                "exceptional",
                B_INCR},
            {
                "exceptionally",
                B_INCR},
            {
                "extreme",
                B_INCR},
            {
                "extremely",
                B_INCR},
            {
                "fabulously",
                B_INCR},
            {
                "flipping",
                B_INCR},
            {
                "flippin",
                B_INCR},
            {
                "frackin",
                B_INCR},
            {
                "fracking",
                B_INCR},
            {
                "fricking",
                B_INCR},
            {
                "frickin",
                B_INCR},
            {
                "frigging",
                B_INCR},
            {
                "friggin",
                B_INCR},
            {
                "fully",
                B_INCR},
            {
                "fuckin",
                B_INCR},
            {
                "fucking",
                B_INCR},
            {
                "fuggin",
                B_INCR},
            {
                "fugging",
                B_INCR},
            {
                "greatly",
                B_INCR},
            {
                "hella",
                B_INCR},
            {
                "highly",
                B_INCR},
            {
                "hugely",
                B_INCR},
            {
                "incredible",
                B_INCR},
            {
                "incredibly",
                B_INCR},
            {
                "intensely",
                B_INCR},
            {
                "major",
                B_INCR},
            {
                "majorly",
                B_INCR},
            {
                "more",
                B_INCR},
            {
                "most",
                B_INCR},
            {
                "particularly",
                B_INCR},
            {
                "purely",
                B_INCR},
            {
                "quite",
                B_INCR},
            {
                "really",
                B_INCR},
            {
                "remarkably",
                B_INCR},
            {
                "so",
                B_INCR},
            {
                "substantially",
                B_INCR},
            {
                "thoroughly",
                B_INCR},
            {
                "total",
                B_INCR},
            {
                "totally",
                B_INCR},
            {
                "tremendous",
                B_INCR},
            {
                "tremendously",
                B_INCR},
            {
                "uber",
                B_INCR},
            {
                "unbelievably",
                B_INCR},
            {
                "unusually",
                B_INCR},
            {
                "utter",
                B_INCR},
            {
                "utterly",
                B_INCR},
            {
                "very",
                B_INCR},
            {
                "almost",
                B_DECR},
            {
                "barely",
                B_DECR},
            {
                "hardly",
                B_DECR},
            {
                "just enough",
                B_DECR},
            {
                "kind of",
                B_DECR},
            {
                "kinda",
                B_DECR},
            {
                "kindof",
                B_DECR},
            {
                "kind-of",
                B_DECR},
            {
                "less",
                B_DECR},
            {
                "little",
                B_DECR},
            {
                "marginal",
                B_DECR},
            {
                "marginally",
                B_DECR},
            {
                "occasional",
                B_DECR},
            {
                "occasionally",
                B_DECR},
            {
                "partly",
                B_DECR},
            {
                "scarce",
                B_DECR},
            {
                "scarcely",
                B_DECR},
            {
                "slight",
                B_DECR},
            {
                "slightly",
                B_DECR},
            {
                "somewhat",
                B_DECR},
            {
                "sort of",
                B_DECR},
            {
                "sorta",
                B_DECR},
            {
                "sortof",
                B_DECR},
            {
                "sort-of",
                B_DECR}};
        
        public static object SENTIMENT_LADEN_IDIOMS = new Dictionary<object, object> {
            {
                "cut the mustard",
                2},
            {
                "hand to mouth",
                -2},
            {
                "back handed",
                -2},
            {
                "blow smoke",
                -2},
            {
                "blowing smoke",
                -2},
            {
                "upper hand",
                1},
            {
                "break a leg",
                2},
            {
                "cooking with gas",
                2},
            {
                "in the black",
                2},
            {
                "in the red",
                -2},
            {
                "on the ball",
                2},
            {
                "under the weather",
                -2}};
        
        public static object SPECIAL_CASES = new Dictionary<object, object> {
            {
                "the shit",
                3},
            {
                "the bomb",
                3},
            {
                "bad ass",
                1.5},
            {
                "badass",
                1.5},
            {
                "bus stop",
                0.0},
            {
                "yeah right",
                -2},
            {
                "kiss of death",
                -1.5},
            {
                "to die for",
                3},
            {
                "beating heart",
                3.5}};
        
        // #Static methods# #
        // 
        //     Determine if input contains negation words
        //     
        public static object negated(object input_words, object include_nt = true) {
            input_words = (from w in input_words
                select w.ToString().lower()).ToList();
            var neg_words = new List<object>();
            neg_words.extend(NEGATE);
            foreach (var word in neg_words) {
                if (input_words.Contains(word)) {
                    return true;
                }
            }
            if (include_nt) {
                foreach (var word in input_words) {
                    if (word.Contains("n't")) {
                        return true;
                    }
                }
            }
            @"if ""least"" in input_words:
        i = input_words.index(""least"")
        if i > 0 and input_words[i - 1] != ""at"":
            return True";
            return false;
        }
        
        // 
        //     Normalize the score to be between -1 and 1 using an alpha that
        //     approximates the max expected value
        //     
        public static object normalize(object score, object alpha = 15) {
            var norm_score = score / math.sqrt(score * score + alpha);
            if (norm_score < -1.0) {
                return -1.0;
            } else if (norm_score > 1.0) {
                return 1.0;
            } else {
                return norm_score;
            }
        }
        
        // 
        //     Check whether just some words in the input are ALL CAPS
        //     :param list words: The words to inspect
        //     :returns: `True` if some but not all items in `words` are ALL CAPS
        //     
        public static object allcap_differential(object words) {
            var is_different = false;
            var allcap_words = 0;
            foreach (var word in words) {
                if (word.isupper()) {
                    allcap_words += 1;
                }
            }
            var cap_differential = words.Count - allcap_words;
            if (0 < cap_differential < words.Count) {
                is_different = true;
            }
            return is_different;
        }
        
        // 
        //     Check if the preceding words increase, decrease, or negate/nullify the
        //     valence
        //     
        public static object scalar_inc_dec(object word, object valence, object is_cap_diff) {
            var scalar = 0.0;
            var word_lower = word.lower();
            if (BOOSTER_DICT.Contains(word_lower)) {
                scalar = BOOSTER_DICT[word_lower];
                if (valence < 0) {
                    scalar *= -1;
                }
                // check if booster/dampener word is in ALLCAPS (while others aren't)
                if (word.isupper() && is_cap_diff) {
                    if (valence > 0) {
                        scalar += C_INCR;
                    } else {
                        scalar -= C_INCR;
                    }
                }
            }
            return scalar;
        }
        
        // 
        //     Identify sentiment-relevant string-level properties of input text.
        //     
        public class SentiText
            : object {
            
            public SentiText(object text) {
                if (!(text is str)) {
                    text = text.ToString().encode("utf-8");
                }
                this.text = text;
                this.words_and_emoticons = this._words_and_emoticons();
                // doesn't separate words from\
                // adjacent punctuation (keeps emoticons & contractions)
                this.is_cap_diff = allcap_differential(this.words_and_emoticons);
            }
            
            // 
            //         Removes all trailing and leading punctuation
            //         If the resulting string has two or fewer characters,
            //         then it was likely an emoticon, so return original string
            //         (ie ":)" stripped would be "", so just return ":)"
            //         
            [staticmethod]
            public static object _strip_punc_if_word(object token) {
                var stripped = token.strip(@string.punctuation);
                if (stripped.Count <= 2) {
                    return token;
                }
                return stripped;
            }
            
            // 
            //         Removes leading and trailing puncutation
            //         Leaves contractions and most emoticons
            //             Does not preserve punc-plus-letter emoticons (e.g. :D)
            //         
            public virtual object _words_and_emoticons() {
                var wes = this.text.split();
                var stripped = map(this._strip_punc_if_word, wes).ToList();
                return stripped;
            }
        }
        
        // 
        //     Give a sentiment intensity score to sentences.
        //     
        public class SentimentIntensityAnalyzer
            : object {
            
            public SentimentIntensityAnalyzer(object lexicon_file = "vader_lexicon.txt", object emoji_lexicon = "emoji_utf8_lexicon.txt") {
                var _this_module_file_path_ = os.path.abspath(getsourcefile(() => 0));
                var lexicon_full_filepath = os.path.join(os.path.dirname(_this_module_file_path_), lexicon_file);
                using (var f = codecs.open(lexicon_full_filepath, encoding: "utf-8")) {
                    this.lexicon_full_filepath = f.read();
                }
                this.lexicon = this.make_lex_dict();
                var emoji_full_filepath = os.path.join(os.path.dirname(_this_module_file_path_), emoji_lexicon);
                using (var f = codecs.open(emoji_full_filepath, encoding: "utf-8")) {
                    this.emoji_full_filepath = f.read();
                }
                this.emojis = this.make_emoji_dict();
            }
            
            // 
            //         Convert lexicon file to a dictionary
            //         
            public virtual object make_lex_dict() {
                var lex_dict = new Dictionary<object, object> {
                };
                foreach (var line in this.lexicon_full_filepath.rstrip("\n").split("\n")) {
                    if (!line) {
                        continue;
                    }
                    (word, measure) = line.strip().split("\t")[0::2];
                    lex_dict[word] = float(measure);
                }
                return lex_dict;
            }
            
            // 
            //         Convert emoji lexicon file to a dictionary
            //         
            public virtual object make_emoji_dict() {
                var emoji_dict = new Dictionary<object, object> {
                };
                foreach (var line in this.emoji_full_filepath.rstrip("\n").split("\n")) {
                    (emoji, description) = line.strip().split("\t")[0::2];
                    emoji_dict[emoji] = description;
                }
                return emoji_dict;
            }
            
            // 
            //         Return a float for sentiment strength based on the input text.
            //         Positive values are positive valence, negative value are negative
            //         valence.
            //         
            public virtual object polarity_scores(object text) {
                // convert emojis to their textual descriptions
                var text_no_emoji = "";
                var prev_space = true;
                foreach (var chr in text) {
                    if (this.emojis.Contains(chr)) {
                        // get the textual description
                        var description = this.emojis[chr];
                        if (!prev_space) {
                            text_no_emoji += " ";
                        }
                        text_no_emoji += description;
                        prev_space = false;
                    } else {
                        text_no_emoji += chr;
                        prev_space = chr == " ";
                    }
                }
                text = text_no_emoji.strip();
                var sentitext = SentiText(text);
                var sentiments = new List<object>();
                var words_and_emoticons = sentitext.words_and_emoticons;
                foreach (var _tup_1 in words_and_emoticons.Select((_p_1,_p_2) => Tuple.Create(_p_2, _p_1))) {
                    var i = _tup_1.Item1;
                    var item = _tup_1.Item2;
                    var valence = 0;
                    // check for vader_lexicon words that may be used as modifiers or negations
                    if (BOOSTER_DICT.Contains(item.lower())) {
                        sentiments.append(valence);
                        continue;
                    }
                    if (i < words_and_emoticons.Count - 1 && item.lower() == "kind" && words_and_emoticons[i + 1].lower() == "of") {
                        sentiments.append(valence);
                        continue;
                    }
                    sentiments = this.sentiment_valence(valence, sentitext, item, i, sentiments);
                }
                sentiments = this._but_check(words_and_emoticons, sentiments);
                var valence_dict = this.score_valence(sentiments, text);
                return valence_dict;
            }
            
            public virtual object sentiment_valence(
                object valence,
                object sentitext,
                object item,
                object i,
                object sentiments) {
                var is_cap_diff = sentitext.is_cap_diff;
                var words_and_emoticons = sentitext.words_and_emoticons;
                var item_lowercase = item.lower();
                if (this.lexicon.Contains(item_lowercase)) {
                    // get the sentiment valence 
                    valence = this.lexicon[item_lowercase];
                    // check for "no" as negation for an adjacent lexicon item vs "no" as its own stand-alone lexicon item
                    if (item_lowercase == "no" && i != words_and_emoticons.Count - 1 && this.lexicon.Contains(words_and_emoticons[i + 1].lower())) {
                        // don't use valence of "no" as a lexicon item. Instead set it's valence to 0.0 and negate the next item
                        valence = 0.0;
                    }
                    if (i > 0 && words_and_emoticons[i - 1].lower() == "no" || i > 1 && words_and_emoticons[i - 2].lower() == "no" || i > 2 && words_and_emoticons[i - 3].lower() == "no" && new List<object> {
                        "or",
                        "nor"
                    }.Contains(words_and_emoticons[i - 1].lower())) {
                        valence = this.lexicon[item_lowercase] * N_SCALAR;
                    }
                    // check if sentiment laden word is in ALL CAPS (while others aren't)
                    if (item.isupper() && is_cap_diff) {
                        if (valence > 0) {
                            valence += C_INCR;
                        } else {
                            valence -= C_INCR;
                        }
                    }
                    foreach (var start_i in Enumerable.Range(0, 3 - 0)) {
                        // dampen the scalar modifier of preceding words and emoticons
                        // (excluding the ones that immediately preceed the item) based
                        // on their distance from the current item.
                        if (i > start_i && !this.lexicon.Contains(words_and_emoticons[i - (start_i + 1)].lower())) {
                            var s = scalar_inc_dec(words_and_emoticons[i - (start_i + 1)], valence, is_cap_diff);
                            if (start_i == 1 && s != 0) {
                                s = s * 0.95;
                            }
                            if (start_i == 2 && s != 0) {
                                s = s * 0.9;
                            }
                            valence = valence + s;
                            valence = this._negation_check(valence, words_and_emoticons, start_i, i);
                            if (start_i == 2) {
                                valence = this._special_idioms_check(valence, words_and_emoticons, i);
                            }
                        }
                    }
                    valence = this._least_check(valence, words_and_emoticons, i);
                }
                sentiments.append(valence);
                return sentiments;
            }
            
            public virtual object _least_check(object valence, object words_and_emoticons, object i) {
                // check for negation case using "least"
                if (i > 1 && !this.lexicon.Contains(words_and_emoticons[i - 1].lower()) && words_and_emoticons[i - 1].lower() == "least") {
                    if (words_and_emoticons[i - 2].lower() != "at" && words_and_emoticons[i - 2].lower() != "very") {
                        valence = valence * N_SCALAR;
                    }
                } else if (i > 0 && !this.lexicon.Contains(words_and_emoticons[i - 1].lower()) && words_and_emoticons[i - 1].lower() == "least") {
                    valence = valence * N_SCALAR;
                }
                return valence;
            }
            
            [staticmethod]
            public static object _but_check(object words_and_emoticons, object sentiments) {
                // check for modification in sentiment due to contrastive conjunction 'but'
                var words_and_emoticons_lower = (from w in words_and_emoticons
                    select w.ToString().lower()).ToList();
                if (words_and_emoticons_lower.Contains("but")) {
                    var bi = words_and_emoticons_lower.index("but");
                    foreach (var sentiment in sentiments) {
                        var si = sentiments.index(sentiment);
                        if (si < bi) {
                            sentiments.pop(si);
                            sentiments.insert(si, sentiment * 0.5);
                        } else if (si > bi) {
                            sentiments.pop(si);
                            sentiments.insert(si, sentiment * 1.5);
                        }
                    }
                }
                return sentiments;
            }
            
            [staticmethod]
            public static object _special_idioms_check(object valence, object words_and_emoticons, object i) {
                var words_and_emoticons_lower = (from w in words_and_emoticons
                    select w.ToString().lower()).ToList();
                var onezero = "{0} {1}".format(words_and_emoticons_lower[i - 1], words_and_emoticons_lower[i]);
                var twoonezero = "{0} {1} {2}".format(words_and_emoticons_lower[i - 2], words_and_emoticons_lower[i - 1], words_and_emoticons_lower[i]);
                var twoone = "{0} {1}".format(words_and_emoticons_lower[i - 2], words_and_emoticons_lower[i - 1]);
                var threetwoone = "{0} {1} {2}".format(words_and_emoticons_lower[i - 3], words_and_emoticons_lower[i - 2], words_and_emoticons_lower[i - 1]);
                var threetwo = "{0} {1}".format(words_and_emoticons_lower[i - 3], words_and_emoticons_lower[i - 2]);
                var sequences = new List<object> {
                    onezero,
                    twoonezero,
                    twoone,
                    threetwoone,
                    threetwo
                };
                foreach (var seq in sequences) {
                    if (SPECIAL_CASES.Contains(seq)) {
                        valence = SPECIAL_CASES[seq];
                        break;
                    }
                }
                if (words_and_emoticons_lower.Count - 1 > i) {
                    var zeroone = "{0} {1}".format(words_and_emoticons_lower[i], words_and_emoticons_lower[i + 1]);
                    if (SPECIAL_CASES.Contains(zeroone)) {
                        valence = SPECIAL_CASES[zeroone];
                    }
                }
                if (words_and_emoticons_lower.Count - 1 > i + 1) {
                    var zeroonetwo = "{0} {1} {2}".format(words_and_emoticons_lower[i], words_and_emoticons_lower[i + 1], words_and_emoticons_lower[i + 2]);
                    if (SPECIAL_CASES.Contains(zeroonetwo)) {
                        valence = SPECIAL_CASES[zeroonetwo];
                    }
                }
                // check for booster/dampener bi-grams such as 'sort of' or 'kind of'
                var n_grams = new List<object> {
                    threetwoone,
                    threetwo,
                    twoone
                };
                foreach (var n_gram in n_grams) {
                    if (BOOSTER_DICT.Contains(n_gram)) {
                        valence = valence + BOOSTER_DICT[n_gram];
                    }
                }
                return valence;
            }
            
            [staticmethod]
            public static object _sentiment_laden_idioms_check(object valence, object senti_text_lower) {
                // Future Work
                // check for sentiment laden idioms that don't contain a lexicon word
                var idioms_valences = new List<object>();
                foreach (var idiom in SENTIMENT_LADEN_IDIOMS) {
                    if (senti_text_lower.Contains(idiom)) {
                        Console.WriteLine(idiom, senti_text_lower);
                        valence = SENTIMENT_LADEN_IDIOMS[idiom];
                        idioms_valences.append(valence);
                    }
                }
                if (idioms_valences.Count > 0) {
                    valence = idioms_valences.Sum() / float(idioms_valences.Count);
                }
                return valence;
            }
            
            [staticmethod]
            public static object _negation_check(object valence, object words_and_emoticons, object start_i, object i) {
                var words_and_emoticons_lower = (from w in words_and_emoticons
                    select w.ToString().lower()).ToList();
                if (start_i == 0) {
                    if (negated(new List<object> {
                        words_and_emoticons_lower[i - (start_i + 1)]
                    })) {
                        // 1 word preceding lexicon word (w/o stopwords)
                        valence = valence * N_SCALAR;
                    }
                }
                if (start_i == 1) {
                    if (words_and_emoticons_lower[i - 2] == "never" && (words_and_emoticons_lower[i - 1] == "so" || words_and_emoticons_lower[i - 1] == "this")) {
                        valence = valence * 1.25;
                    } else if (words_and_emoticons_lower[i - 2] == "without" && words_and_emoticons_lower[i - 1] == "doubt") {
                        valence = valence;
                    } else if (negated(new List<object> {
                        words_and_emoticons_lower[i - (start_i + 1)]
                    })) {
                        // 2 words preceding the lexicon word position
                        valence = valence * N_SCALAR;
                    }
                }
                if (start_i == 2) {
                    if (words_and_emoticons_lower[i - 3] == "never" && (words_and_emoticons_lower[i - 2] == "so" || words_and_emoticons_lower[i - 2] == "this") || (words_and_emoticons_lower[i - 1] == "so" || words_and_emoticons_lower[i - 1] == "this")) {
                        valence = valence * 1.25;
                    } else if (words_and_emoticons_lower[i - 3] == "without" && (words_and_emoticons_lower[i - 2] == "doubt" || words_and_emoticons_lower[i - 1] == "doubt")) {
                        valence = valence;
                    } else if (negated(new List<object> {
                        words_and_emoticons_lower[i - (start_i + 1)]
                    })) {
                        // 3 words preceding the lexicon word position
                        valence = valence * N_SCALAR;
                    }
                }
                return valence;
            }
            
            public virtual object _punctuation_emphasis(object text) {
                // add emphasis from exclamation points and question marks
                var ep_amplifier = this._amplify_ep(text);
                var qm_amplifier = this._amplify_qm(text);
                var punct_emph_amplifier = ep_amplifier + qm_amplifier;
                return punct_emph_amplifier;
            }
            
            [staticmethod]
            public static object _amplify_ep(object text) {
                // check for added emphasis resulting from exclamation points (up to 4 of them)
                var ep_count = text.count("!");
                if (ep_count > 4) {
                    ep_count = 4;
                }
                // (empirically derived mean sentiment intensity rating increase for
                // exclamation points)
                var ep_amplifier = ep_count * 0.292;
                return ep_amplifier;
            }
            
            [staticmethod]
            public static object _amplify_qm(object text) {
                // check for added emphasis resulting from question marks (2 or 3+)
                var qm_count = text.count("?");
                var qm_amplifier = 0;
                if (qm_count > 1) {
                    if (qm_count <= 3) {
                        // (empirically derived mean sentiment intensity rating increase for
                        // question marks)
                        qm_amplifier = qm_count * 0.18;
                    } else {
                        qm_amplifier = 0.96;
                    }
                }
                return qm_amplifier;
            }
            
            [staticmethod]
            public static object _sift_sentiment_scores(object sentiments) {
                // want separate positive versus negative sentiment scores
                var pos_sum = 0.0;
                var neg_sum = 0.0;
                var neu_count = 0;
                foreach (var sentiment_score in sentiments) {
                    if (sentiment_score > 0) {
                        pos_sum += float(sentiment_score) + 1;
                    }
                    if (sentiment_score < 0) {
                        neg_sum += float(sentiment_score) - 1;
                    }
                    if (sentiment_score == 0) {
                        neu_count += 1;
                    }
                }
                return Tuple.Create(pos_sum, neg_sum, neu_count);
            }
            
            public virtual object score_valence(object sentiments, object text) {
                object neu;
                object neg;
                object pos;
                object compound;
                if (sentiments) {
                    var sum_s = float(sentiments.Sum());
                    // compute and add emphasis from punctuation in text
                    var punct_emph_amplifier = this._punctuation_emphasis(text);
                    if (sum_s > 0) {
                        sum_s += punct_emph_amplifier;
                    } else if (sum_s < 0) {
                        sum_s -= punct_emph_amplifier;
                    }
                    compound = normalize(sum_s);
                    // discriminate between positive, negative and neutral sentiment scores
                    var _tup_1 = this._sift_sentiment_scores(sentiments);
                    var pos_sum = _tup_1.Item1;
                    var neg_sum = _tup_1.Item2;
                    var neu_count = _tup_1.Item3;
                    if (pos_sum > math.fabs(neg_sum)) {
                        pos_sum += punct_emph_amplifier;
                    } else if (pos_sum < math.fabs(neg_sum)) {
                        neg_sum -= punct_emph_amplifier;
                    }
                    var total = pos_sum + math.fabs(neg_sum) + neu_count;
                    pos = math.fabs(pos_sum / total);
                    neg = math.fabs(neg_sum / total);
                    neu = math.fabs(neu_count / total);
                } else {
                    compound = 0.0;
                    pos = 0.0;
                    neg = 0.0;
                    neu = 0.0;
                }
                var sentiment_dict = new Dictionary<object, object> {
                    {
                        "neg",
                        round(neg, 3)},
                    {
                        "neu",
                        round(neu, 3)},
                    {
                        "pos",
                        round(pos, 3)},
                    {
                        "compound",
                        round(compound, 4)}};
                return sentiment_dict;
            }
        }
        
        public static object sentences = new List<object> {
            "VADER is smart, handsome, and funny.",
            "VADER is smart, handsome, and funny!",
            "VADER is very smart, handsome, and funny.",
            "VADER is VERY SMART, handsome, and FUNNY.",
            "VADER is VERY SMART, handsome, and FUNNY!!!",
            "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
            "VADER is not smart, handsome, nor funny.",
            "The book was good.",
            "At least it isn't a horrible book.",
            "The book was only kind of good.",
            "The plot was good, but the characters are uncompelling and the dialog is not great.",
            "Today SUX!",
            "Today only kinda sux! But I'll get by, lol",
            "Make sure you :) or :D today!",
            "Catch utf-8 emoji such as 💘 and 💋 and 😁",
            "Not bad at all"
        };
        
        public static object analyzer = SentimentIntensityAnalyzer();
        
        public static object vs = analyzer.polarity_scores(sentence);
        
        public static object tricky_sentences = new List<object> {
            "Sentiment analysis has never been good.",
            "Sentiment analysis has never been this good!",
            "Most automated sentiment analysis tools are shit.",
            "With VADER, sentiment analysis is the shit!",
            "Other sentiment analysis tools can be quite bad.",
            "On the other hand, VADER is quite bad ass",
            "VADER is such a badass!",
            "Without a doubt, excellent idea.",
            "Roger Dodger is one of the most compelling variations on this theme.",
            "Roger Dodger is at least compelling as a variation on the theme.",
            "Roger Dodger is one of the least compelling variations on this theme.",
            "Not such a badass after all.",
            "Without a doubt, an excellent idea."
        };
        
        public static object vs = analyzer.polarity_scores(sentence);
        
        public static object paragraph = "It was one of the worst movies I've seen, despite good reviews. Unbelievably bad acting!! Poor direction. VERY poor production. The movie was bad. Very bad movie. VERY BAD movie!";
        
        public static object sentence_list = tokenize.sent_tokenize(paragraph);
        
        public static object paragraphSentiments = 0.0;
        
        public static object vs = analyzer.polarity_scores(sentence);
        
        public static object paragraphSentiments = vs["compound"];
        
        public static object conceptList = new List<object> {
            "balloons",
            "cake",
            "candles",
            "happy birthday",
            "friends",
            "laughing",
            "smiling",
            "party"
        };
        
        public static object conceptSentiments = 0.0;
        
        public static object vs = analyzer.polarity_scores(concept);
        
        public static object conceptSentiments = vs["compound"];
        
        public static object conceptList = new List<object> {
            "riot",
            "fire",
            "fight",
            "blood",
            "mob",
            "war",
            "police",
            "tear gas"
        };
        
        public static object conceptSentiments = 0.0;
        
        public static object vs = analyzer.polarity_scores(concept);
        
        public static object conceptSentiments = vs["compound"];
        
        public static object do_translate = input("\nWould you like to run VADER demo examples with NON-ENGLISH text? \n (Note: requires Internet access and uses the 'requests' library) \n Type 'y' or 'n', then press Enter: ");
        
        public static object languages = new List<object> {
            "English",
            "French",
            "German",
            "Spanish",
            "Italian",
            "Russian",
            "Japanese",
            "Arabic",
            "Chinese(Simplified)",
            "Chinese(Traditional)"
        };
        
        public static object language_codes = new List<object> {
            "en",
            "fr",
            "de",
            "es",
            "it",
            "ru",
            "ja",
            "ar",
            "zh-CN",
            "zh-TW"
        };
        
        public static object nonEnglish_sentences = new List<object> {
            "I'm surprised to see just how amazingly helpful VADER is!",
            "Je suis surpris de voir comment VADER est incroyablement utile !",
            "Ich bin überrascht zu sehen, nur wie erstaunlich nützlich VADER!",
            "Me sorprende ver sólo cómo increíblemente útil VADER!",
            "Sono sorpreso di vedere solo come incredibilmente utile VADER è!",
            "Я удивлен увидеть, как раз как удивительно полезно ВЕЙДЕРА!",
            "私はちょうどどのように驚くほど役に立つベイダーを見て驚いています!",
            "أنا مندهش لرؤية فقط كيف مثير للدهشة فيدر فائدة!",
            "我很惊讶地看到VADER是如此有用!",
            "我很驚訝地看到VADER是如此有用!"
        };
        
        public static object to_lang = "en";
        
        public static object from_lang = language_codes[nonEnglish_sentences.index(sentence)];
        
        public static object translation = sentence;
        
        public static object translator_name = "No translation needed";
        
        public static object api_url = "http://mymemory.translated.net/api/get?q={}&langpair={}|{}".format(sentence, from_lang, to_lang);
        
        public static object hdrs = new Dictionary<object, object> {
            {
                "User-Agent",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"},
            {
                "Accept",
                "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"},
            {
                "Accept-Charset",
                "ISO-8859-1,utf-8;q=0.7,*;q=0.3"},
            {
                "Accept-Encoding",
                "none"},
            {
                "Accept-Language",
                "en-US,en;q=0.8"},
            {
                "Connection",
                "keep-alive"}};
        
        public static object response = requests.get(api_url, headers: hdrs);
        
        public static object response_json = json.loads(response.text);
        
        public static object translation = response_json["responseData"]["translatedText"];
        
        public static object translator_name = "MemoryNet Translation Service";
        
        public static object vs = analyzer.polarity_scores(translation);
    }
}
