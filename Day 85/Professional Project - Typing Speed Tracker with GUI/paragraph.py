import random


class Paragraph:
    def __init__(self):
        self.paragraph_list = [

            "Devon couldn't figure out the color of her eyes. \
                He initially would have guessed that they were green, \
                    but the more he looked at them he almost wanted to say they were a golden yellow. \
                        Then there were the flashes of red and orange \
                            that seemed to be streaked throughout them.",

            "It was almost as if her eyes were made of opal with the sun \
                constantly glinting off of them and bringing out more color. \
                    They were definitely the most unusual pair of eyes he'd ever seen. \
                        At that moment, she realized that she had created her current life. \
                            It wasn't the life she wanted, \
                                but she took responsibility for how it currently stood.",

            "Something clicked and she saw that every choice she made \
                to this point in her life had led to where her life stood at \
                    this very moment even if she knew this wasn't where she wanted to be. \
                        She determined to choose to change it. There was nothing else to do. \
                            The deed had already been done and there was no going back.",

            "It now had been become a question of how they were going \
                to be able to get out of this situation and escape. \
                    There wasn't a whole lot more that could be done. \
                        It had become a wait-and-see situation with the final \
                            results no longer in her control. \
                                That didn't stop her from trying to control the situation.",

            "She demanded that things be done as she desperately \
                tried to control what couldn't be. The wolves stopped \
                    in their tracks, sizing up the mother and her cubs. \
                        It had been over a week since their last meal and \
                            they were getting desperate. The cubs would make a \
                                good meal, but there were high risks taking on the mother Grizzly.",

            "A decision had to be made and the wrong choice \
                could signal the end of the pack. I don't like \
                    cats and they don't like me. I used to be allergic \
                        to them and I would get stuffed up and have hives. \
                            That doesn't seem to happen anymore. But I still don't like them. \
                                I lived with 3 cats that were not good at peeing in the litter box.",

            "They seemed to find something important to me and pee on it. \
                Most of the time they peed on photographs or papers that would be ruined. \
                    Cats also bring fleas into the house. \
                        There is nothing worse than having to flea dip cats and also flea bomb a home. \
                            That is why I don't like cats.",

            '''"What is the best way to get what you want?" she asked. \
                He looked down at the ground knowing that she wouldn't like his answer. \
                    He hesitated, knowing that the truth would only hurt. \
                        How was he going to tell her that the best way for him to \
                            get what he wanted was to leave her?''',

            'Twenty-five stars were neatly placed on the piece of paper. \
                There was room for five more stars but they would be difficult ones to earn. \
                    It had taken years to earn the first twenty-five, \
                        and they were considered the "easy" ones. It was a simple green chair. \
                            There was nothing extraordinary about it or so it seemed.',

            "It was the type of chair one would pass without even noticing it was there, \
                let alone what the actual color of it was. \
                    It was due to this common and unassuming appearance \
                        that few people actually stopped to sit in it and discover its magical powers. \
                            It really didn't matter what they did to him. \
                                He's already made up his mind.",

            "Whatever came his way, he was prepared for the consequences. \
                He knew in his heart that the sacrifice he made was done with \
                    love and not hate no matter how others decided to spin it. \
                        Mary had to make a decision and she knew that whatever decision she made, \
                            it would upset someone.",

            "It seemed like such a silly reason for people to get upset but \
                she knew the minute that she began to consider doing it that \
                    there was no way everyone in her life would be pleased with \
                        what she ultimately decided to do. \
                            It was simply a question of who she would rather displease most.",

            "While this had always been her parents, and especially her mom, \
                in the past that she tried to keep from upsetting, \
                    she decided that this time the person she was going \
                        to please the most with her decision was herself. \
                            There are only three ways to make this work. \
                                The first is to let me take care of everything.",

            "The second is for you to take care of everything. \
                The third is to split everything 50 / 50. \
                    I think the last option is the most preferable, \
                        but I'm certain it'll also mean the end of our marriage. \
                            It was a good idea. \
                                At least, they all thought it was a good idea at the time.",

            "Hindsight would reveal that in reality, it was an unbelievably terrible idea, \
                but it would take another week for them to understand that. \
                    Right now, at this very moment, \
                        they all agreed that it was the perfect \
                            course of action for the current situation. \
                                Brock would have never dared to do it \
                                    zon his own he thought to himself.",

            "That is why Kenneth and he had become such good friends. \
                Kenneth forced Brock out of his comfort zone and made him \
                    try new things he'd never imagine doing otherwise. \
                        Up to this point, this had been a good thing. \
                            It had expanded Brock's experiences and \
                                given him a new appreciation for life.",

            "Now that both of them were in the back of a police car, \
                all Brock could think was that he would have never dared \
                    do it except for the influence of Kenneth. It was easy to spot her. \
                        All you needed to do was look at her socks. \
                            They were never a matching pair. \
                                One would be green while the other would be blue.",

            "One would reach her knee while the other barely touched her ankle. \
                Every other part of her was perfect, but never the socks. \
                    They were her micro act of rebellion. It wasn't quite yet time to panic. \
                        There was still time to salvage the situation. \
                            At least that is what she was telling himself.",

            "The reality was that it was time to panic and \
                there wasn't time to salvage the situation, \
                    but he continued to delude himself into believing there was. \
                        The cab arrived late. \
                            The inside was in as bad of shape as the outside which was concerning, \
                                and it didn't appear that it had been cleaned in months.",

            "The green tree air-freshener hanging from the rearview \
                mirror was either exhausted of its scent or not strong \
                    enough to overcome the other odors emitting from the cab. \
                        The correct decision, in this case, \
                            was to get the hell out of it and to call another cab, \
                                but she was late and didn't have a choice.",

            "I'm heading back to Colorado tomorrow after being down \
                in Santa Barbara over the weekend for the festival there. \
                    I will be making October plans once there and will try to \
                        arrange so I'm back here for the birthday if possible. \
                            I'll let you know as soon as I know the doctor's \
                                appointment schedule and my flight plans.",

            "There was a reason for her shyness. \
                Everyone assumed it had always been there but she knew better. \
                    She knew the exact moment that the shyness began. \
                        It had been that fateful moment at the lake. \
                            There are just some events that do that to you. \
                                All he could think about was how it would all end.",

            "There was still a bit of uncertainty in the equation, \
                but the basics were there for anyone to see. \
                    No matter how much he tried to see the positive, it wasn't anywhere to be seen. \
                        The end was coming and it wasn't going to be pretty. \
                            It was a simple tip of the hat. \
                                Grace didn't think that anyone else besides her had even noticed it.",

            "It wasn't anything that the average person would notice, \
                let alone remember at the end of the day. \
                    That's why it seemed so unbelievable that this little \
                        gesture would ultimately change the course of the world. \
                            Her eyebrows were a shade darker than her hair. \
                                They were thick and almost horizontal, \
                                    emphasizing the depth of her eyes.",

            "She was rather handsome than beautiful. \
                Her face was captivating by reason of a certain \
                    frankness of expression and a contradictory subtle play of features. \
                        Her manner was engaging. The headache wouldn't go away. \
                            She's taken medicine but even that didn't help. \
                                The monstrous throbbing in her head continued.",

            "She had this happen to her only once before in her life \
                and she realized that only one thing could be happening. \
                    he words hadn't flowed from his fingers for the past few weeks. \
                        He never imagined he'd find himself with writer's block, \
                            but here he sat with a blank screen in front of him.",

            "That blank screen taunting him day after day had started to play with his mind. \
                He didn't understand why he couldn't even type a single word, \
                    just one to begin the process and build from there. And yet, \
                        he already knew that the eight hours he was prepared to sit \
                            in front of his computer today would end with the screen remaining blank.",
                            
            "They had made it to Las Vegas, wide-eyed and with so much hope and energy. \
                They had planned the trip for more than a year and \
                    both were so excited they could barely control themselves. \
                        They still hadn't realized that Las Vegas promised a place where dreams come true, \
                            it was actually the place where dreams came to die.",

            "It probably seemed trivial to most people, but it mattered to Tracey. \
                She wasn't sure why it mattered so much to her, \
                    but she understood deep within her being that it mattered to her. \
                        So for the 365th day in a row, Tracey sat down to eat pancakes for breakfast.",

            "She counted. One. She could hear the steps coming closer. Two. \
                Puffs of breath could be seen coming from his mouth. Three. He stopped beside her. Four. \
                    She pulled the trigger of the gun. She was aware that things could go wrong. \
                        In fact, she had trained her entire life in anticipation that things would go wrong one day.", 

            "She had quiet confidence as she started to see that \
                this was the day that all her training would be worthwhile and useful. \
                    At this point, she had no idea just how wrong everything would go that day. \
                        He collected the plastic trash on a daily basis. It never seemed to end.",

            "Even if he cleaned the entire beach, more plastic would cover it the next day after the tide had come in. \
                Although it was a futile effort that would never be done, he continued to pick up the trash each day. \
                    Cake or pie? I can tell a lot about you by which one you pick.",

            "It may seem silly, but cake people and pie people are really different. \
                I know which one I hope you are, but that's not for me to decide. \
                    So, what is it? Cake or pie? The boxed moved. That was a problem. \
                        Peter had packed the box three hours before and there was nothing inside that should make it move.",

            "The question now was whether or not Peter was going to open it up and look inside to see why it had moved. \
                The answer to that question was obvious. \
                    Peter dropped the package into the mailbox so he would never have to see it again. \
                        The paper was blank. It shouldn't have been.", 

            "There should have been writing on the paper, at least a paragraph if not more. \
                The fact that the writing wasn't there was frustrating. Actually, it was even more than frustrating. \
                    It was downright distressing. Dragons don't exist they said. \
                        They are the stuff of legend and people's imagination.",

            "Greg would have agreed with this assessment without a second thought 24 hours ago. \
                But now that there was a dragon staring directly into his eyes, \
                    he questioned everything that he had been told. \
                        He swung back the fishing pole and cast the line which ell 25 feet away into the river.",

            "The lure landed in the perfect spot and he was sure he would soon get a bite. \
                He never expected that the bite would come from behind in the form of a bear. \
                    Debbie had taken George for granted for more than fifteen years now. \
                        He wasn't sure what exactly had made him choose this time and place to address the issue, \
                            but he decided that now was the time.",

            "He looked straight into her eyes and just as she was about to speak, turned away and walked out the door. \
                They decided to find the end of the rainbow. \
                    While they hoped they would find a pot of gold, \
                        neither of them truly believed that the mythical pot would actually be there.",

            "Nor did they believe they could actually find the end of the rainbow. \
                Still, it seemed like a fun activity for the day, \
                    and pictures of them chasing rainbows would look great on their Instagram accounts. \
                        They would have never believed they would actually find the end of a rainbow, \
                            and when they did, what they actually found there.",

            '“Ingredients for life,” said the backside of the truck. \
                They mean food, but really food is only 1 ingredient of life. \
                    Life has so many more ingredients such as pain, happiness, laughter, joy, tears, and smiles. \
                        Life also has hard work, easy play, sleepless nights, and sunbathing by the ocean.',

            "Love, hatred, envy, self-assurance, and fear could be just down aisle 3 ready to be bought when needed. \
                How I wish I could pull ingredients like these off shelves in a store. \
                    You can decide what you want to do in life, but I suggest doing something that creates.",

            '''Something that leaves a tangible thing once you're done. \
                That way even after you're gone, you will still live on in the things you created. \
                    "I'll talk to you tomorrow in more detail at our meeting, \
                        but I think I've found a solution to our problem. \
                            It's not exactly legal, but it won't land us in jail for the rest of our lives either."''',

            '''"Are you willing to take the chance?" Monroe asked his partner over the phone. \
                Dave wasn't exactly sure how he had ended up in this predicament. \
                    He ran through all the events that had lead to this current situation and it still didn't make sense. \
                        He wanted to spend some time to try and make sense of it all, \
                            but he had higher priorities at the moment.''', 

            "The first was how to get out of his current situation of being \
                naked in a tree with snow falling all around and no way for him to get down. \
                    There was something special about this little creature. \
                        Donna couldn't quite pinpoint what it was, but she knew with all her heart that it was true.",

            "It wasn't a matter of if she was going to try and save it, but a matter of how she was going to save it. \
                She went back to the car to get a blanket and when she returned the creature was gone. \
                    Sometimes that's just the way it has to be. \
                        Sure, there were probably other options, but he didn't let them enter his mind.",

            "It was done and that was that. It was just the way it had to be. \
                The blinking light caught her attention. \
                    She thought about it a bit and couldn't remember ever noticing it before. \
                        That was strange since it was obvious the flashing light had been there for years.",

            "Now she wondered how she missed it for that amount of time \
                and what other things in her small town she had failed to notice. \
                    He had three simple rules by which he lived. The first was to never eat blue food. \
                        There was nothing in nature that was edible that was blue.",

            "People often asked about blueberries, but everyone knows those are actually purple. \
                He understood it was one of the stranger rules to live by, \
                    but it had served him well thus far in the 50+ years of his life. \
                        The rain was coming. Everyone thought this would be a good thing.",

            "It hadn't rained in months and the earth was dry as a bone. \
                It wasn't a surprise that everyone thought a good rain was what was needed, \
                    but they never expected how much rain would actually arrive. They argue. \
                        While the argument seems to be different the truth is it's always the same.",

            "Yes, the topic may be different or the circumstances, \
                but when all said and done, it all came back to the same thing. \
                    They both knew it, but neither has the courage or strength to address the underlying issue. \
                        So they continue to argue. He knew what he was supposed to do.",

            "That had been apparent from the beginning. That was what made the choice so difficult. \
                What he was supposed to do and what he would do were not the same. \
                    This would have been fine if he were willing to face the inevitable consequences, but he wasn't. \
                        The water rush down the wash and into the slot canyon below.",

            "Two hikers had started the day to sunny weather without a cloud in the sky, \
                but they hadn't thought to check the weather north of the canyon. \
                    Huge thunderstorms had brought a deluge o rain and produced flash floods heading their way. \
                        The two hikers had no idea what was coming."

                            ]

    def get_random_paragraph(self):
        return random.choice(self.paragraph_list)
