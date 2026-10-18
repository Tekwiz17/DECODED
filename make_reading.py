"""Reusable three-level text authoring. Run after adding notes or a course."""
import runpy,json
ns=runpy.run_path('make_content.py')
easy={
'water':[
'Water is made of two hydrogen atoms and one oxygen atom. Oxygen pulls harder on their shared electrons. The oxygen end becomes a little negative. The hydrogen ends become a little positive. This uneven charge is called polarity.',
'Opposite charges attract. A hydrogen end on one water molecule can attract the oxygen end on another. That attraction is a hydrogen bond. It is different from the stronger bonds holding one water molecule together.',
'Cohesion means water sticks to water. It helps water form drops. Adhesion means water sticks to other things, like glass. These two effects help water move through tiny spaces in plants.',
'Water takes a lot of heat to warm up. That helps a lake or your body change temperature slowly. When sweat evaporates, it carries heat away and helps cool you.',
'Water can surround and mix with many charged or polar particles. Oil does not mix well with water. When water freezes, its molecules spread into a more open pattern. Ice takes up more space for the same amount of water, so it floats.'],
'ph':[
'pH tells you how acidic or basic a liquid is. At about room temperature, below 7 is acidic, 7 is neutral, and above 7 is basic. A lower pH means more hydrogen ions, written H⁺. Acids increase H⁺. Bases reduce H⁺.',
'Each step on the pH scale means ten times. pH 3 has ten times more H⁺ than pH 4. It has 100 times more than pH 5. Think: one step is ×10, two steps are ×100.',
'Cells need the right conditions to work. A big pH change can change a protein’s shape. A buffer helps stop pH from changing too much. It does not always make the liquid neutral.',
'An indicator is a color-changing clue. Iodine turns blue-black when starch is present. Heated Benedict’s solution can show simple sugars such as glucose. Litmus and phenolphthalein help test acids or bases. Bromothymol blue changes with pH. Dissolved CO₂ can make pH lower. Compare your sample with known examples to check the result.'],
'building':[
'A monomer is one small building block. A polymer is many repeating blocks joined together. Sugar blocks can make large carbohydrates. Amino acids make protein chains. Nucleotides make DNA and RNA. Lipids are different: they are not repeating-block chains.',
'To join two blocks, a bond forms between them. In our simple model, an H and an OH come off the blocks and make water. The blocks join and water comes out. This is dehydration synthesis.',
'To split a link, water is used. Water supplies H and OH to the pieces. This is hydrolysis. Your body uses it during digestion to break big food molecules into smaller pieces.',
'Count the spaces between the blocks. Five blocks in one straight chain need four links. Making those four links releases four waters in our model. Breaking the four links uses four waters.'],
'molecules':[
'Carbohydrates include sugars and chains of sugars. Glucose is one sugar. Starch stores sugar in plants. Glycogen stores sugar in animals. Cellulose helps make plant cell walls strong.',
'Lipids include fats and oils. Fats store energy, help keep heat in, and cushion body parts. One fat called a triglyceride has a glycerol part and three fatty acid tails. Other lipids help build the outside boundary of cells.',
'Saturated fat tails have no carbon–carbon double bonds and can pack closely. Cis unsaturated tails have bends at double bonds, so they cannot pack as closely. This often makes the fat more fluid. Trans tails are straighter than cis tails.',
'Proteins do many jobs: they can carry things, give support, and help reactions happen. Proteins are made from amino acids. Amino acids share the same basic parts. Their R group is the part that changes.',
'DNA and RNA are nucleic acids. They are made of blocks called nucleotides. Each block has a sugar, a phosphate, and a base. DNA stores inherited instructions. RNA helps cells use those instructions.'],
'proteins':[
'Think of amino acids as beads on a string. Primary structure means the order of the beads. Peptide bonds are the links holding the beads together.',
'Parts of the string can coil or fold into sheets. These small patterns are secondary structure. Hydrogen bonds between parts of the backbone help hold them in place.',
'The whole string folds into a 3D shape. That is tertiary structure. The R groups help decide how it folds. The shape helps the protein do its job.',
'Some proteins use a team of two or more folded strings. That team is quaternary structure. A protein with only one string does not have this level.',
'Heat or a big pH change can make a protein lose its useful shape. This is denaturation. The beads usually stay in the same order, but the protein may stop working. Unfolding is different from cutting the string apart.']}
easy_why=[
'Oxygen pulls harder on shared electrons. That makes one end a little negative and the other ends a little positive. The whole water molecule is still neutral.',
'Ice floats because it is less dense than liquid water. A layer on top can help keep the water below from losing heat as quickly.',
'Adhesion means water sticks to something else. Cohesion means water sticks to water.',
'From pH 5 to pH 3 is two steps down. Each step means ten times more H⁺. So 10 × 10 = 100.',
'Water is a negative control: it shows what the test looks like without the sugar you are looking for.',
'A buffer takes up or releases H⁺ to help keep pH from changing too much.',
'Six blocks need five links to make one straight chain. In our simple model, each new link releases one water.',
'Hydrolysis means using water to split a link. Dehydration synthesis does the reverse: it joins blocks and releases water.',
'Lipids do not form long chains of repeating blocks like proteins, DNA, and many carbohydrates do.',
'Animals store glucose as glycogen. Plants store it as starch. Cellulose supports plant cell walls.',
'A triglyceride has one glycerol part and three fatty acid tails. It is a lipid.',
'Bent tails cannot fit together as tightly. Cis double bonds create these bends.',
'Primary means the order of the amino acid beads. Secondary is small folding patterns. Tertiary is the whole fold. Quaternary is a team of chains.',
'Typical denaturation changes how the chain folds. It usually does not cut the peptide bonds, so the amino acid order stays the same.',
'Hydrogen bonds between backbone groups help hold coils and sheets. These bonds are not between R groups.',
'Two cysteine R groups can join with a strong link called a disulfide bridge. It helps hold the protein’s shape.'
]
easy_prompts=[
'Why does water have a slightly positive end and a slightly negative end?',
'How can floating ice help life in a pond during winter?',
'Water sticks to a glass tube. What is this called?',
'How much more H⁺ does pH 3 have than pH 5?',
'Why test plain water along with a food sample using Benedict’s solution?',
'What does a buffer help do?',
'You join 6 blocks into one straight chain. How many waters come out in our model?',
'Water is used to break a link in a large molecule. What is this called?',
'Which family is NOT a chain of repeating building blocks?',
'Which molecule stores glucose in animals?',
'A molecule has glycerol and three fatty acid tails. What is it?',
'Why do cis unsaturated fat tails often make a fat more fluid?',
'Which protein level means the order of amino acids?',
'After a protein loses its shape from heat, what usually stays the same?',
'What helps hold the small coils and sheets in a protein?',
'What strong link can form between two cysteine R groups?'
]
# Keep question meaning and answer positions unchanged at every reading level.
# Item 9 asks for the pairing; retain its original prompt because its answer options are pairings.
easy_prompts[9]=ns['qs'][9]['prompt']
content={'schemaVersion':1,'levels':['easy','medium','expert'],'topics':{},'questions':[],'terms':{}}
for u in ns['units']:
 id=u['id'];med=u['parts'];expert=ns['expert_parts'][id]
 content['topics'][id]={
  'easy':{'parts':[[med[i][0],p] for i,p in enumerate(easy[id])],'trap':u['trap'],'example':u['example'],'desc':u['desc']},
  'medium':{'parts':med,'trap':u['trap'],'example':u['example'],'desc':u['desc']},
  'expert':{'parts':expert,'trap':u['trap'],'example':u['example'],'desc':u['desc']}
 }
for i,q in enumerate(ns['qs']):content['questions'].append({'easy':{'prompt':easy_prompts[i],'why':easy_why[i]},'medium':{'prompt':q['prompt'],'why':q['why']},'expert':{'prompt':q['prompt'],'why':q['why']}})
terms_easy=['Water sticking to water.','Water sticking to a different surface, like glass.','Something that helps stop pH from changing too much by taking up or releasing H⁺.','Using water to break a link between building blocks.','Joining building blocks and releasing water in our simple model.','Primary is the order of the beads. Tertiary is the whole string’s folded shape.','The part of an amino acid that differs. It helps decide how the protein folds.']
for i,(t,f,b) in enumerate(ns['terms']):content['terms'][f]={'easy':terms_easy[i],'medium':b,'expert':b}
open('public/reading-content.js','w').write('const READING_CONTENT='+json.dumps(content)+';\n')
print('Three reading levels authored for',len(content['topics']),'topics and',len(content['questions']),'questions')
