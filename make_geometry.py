"""Original study content based on the four supplied classroom packets.
Packet order is used for navigation; printed headings differ on packets 3 and 4.
Run python make_geometry.py, then node make_catalog.cjs.
"""
import json
from pathlib import Path
T=[]; Q=[]; C=[]; R={}
def add(unit,id,title,model,parts,trap,example,qs):
 id='geo-'+id
 levels={}
 for k,n in [('easy',1),('medium',2),('expert',3)]:
  levels[k]={'parts':[[p[0],p[n]] for p in parts],'trap':trap,'example':example,'desc':parts[0][n]}
 t={'id':id,'title':title,'desc':parts[0][2],'icon':'◇','group':'Unit '+str(unit),'subject':'geometry','unit':unit,'parts':levels['medium']['parts'],'trap':trap,'example':example,'model':model}
 T.append(t);R[id]=levels
 for i,p in enumerate(parts):C.append({'topic':id,'section':i,'front':p[0]+' — explain it in your own words.','back':p[2]})
 for prompt,options,ans,why in qs:Q.append({'topic':id,'prompt':prompt,'options':options,'answer':ans,'why':why})
add(1,'radicals','Radicals, without the panic','geo-radical',[
('What does a root mean?','√25 asks: what nonnegative number times itself is 25? It is 5. A root undoes a square.','A square root reverses squaring. √a means the principal, nonnegative square root. √25 = 5, while solving x² = 25 gives x = ±5.','For a ≥ 0, √a is the unique nonnegative real number whose square is a. A rational number is a ratio of integers; √2 is irrational, but √9 = 3 is rational.'),
('Pull out a perfect square','Break 72 into 36 × 2. The square root of 36 comes out as 6. So √72 = 6√2.','To simplify √72, find a perfect-square factor: √(36 × 2) = 6√2. Keep factoring until no perfect square greater than 1 remains inside.','For nonnegative a and b, √(ab) = √a √b. Extract the greatest perfect-square factor: √72 = √(36·2) = 6√2. This is an exact value; a rounded decimal is an approximation.'),
('Variables need a small safety check','√(x²) means the distance from zero, so it is |x|. If x cannot be negative, it is just x.','√(x²) = |x|, not always x. For example, if x = −3, the root is 3. If a problem states x ≥ 0, then √(x²) = x.','Because the principal root is nonnegative, √(x²) = |x| for real x. For x ≥ 0, √(18x²) = 3x√2; without that assumption it is 3|x|√2.')],
'√(a + b) is not generally √a + √b. A radical symbol alone gives the nonnegative root.',
'An exact diagonal length such as 6√2 keeps all the precision; 8.49 is only a rounded estimate.',[
('Simplify √50.',['25√2','5√2','10√5','5'],1,'50 = 25 × 2, so √50 = 5√2.'),
('Which number is irrational?',['√49','0.75','√3','−4'],2,'3 is not a perfect square. √3 cannot be written as a ratio of integers.'),
('For any real x, √(x²) equals…',['x','−x','x²','|x|'],3,'The principal square root is nonnegative, so it equals the absolute value of x.')])
add(1,'radical-operations','Add, multiply & rationalize','geo-radical',[
('Only matching roots combine','3√2 + 4√2 = 7√2. The √2 is like a label. A √3 has a different label.','Combine coefficients only when the simplified radicands match. √8 + √18 = 2√2 + 3√2 = 5√2.','Like radicals have the same index and radicand after simplification. Add or subtract their coefficients. Simplification must precede deciding whether radicals are like.'),
('Multiply every needed pair','√3 × √12 = √36 = 6. With brackets, multiply each term, just as you do with numbers.','Multiply coefficients and radicands, then simplify. Use distribution: √2(3 + √2) = 3√2 + 2. For two binomials, multiply all four pairs.','For real square roots with nonnegative radicands, multiply using √a√b = √(ab). Distribution gives (√3 + 2)(√3 − 2) = 3 − 4 = −1.'),
('Clear a root from the bottom','For 1/√2, multiply top and bottom by √2. You get √2/2. You changed the look, not the value.','Rationalize a monomial denominator by multiplying numerator and denominator by a suitable radical. For a binomial use its conjugate: (a + √b)(a − √b) = a² − b.','Multiplying by a nonzero expression divided by itself preserves a fraction. For 1/(√5 + 1), use (√5 − 1)/(√5 − 1), giving (√5 − 1)/4. The original denominator must be nonzero.')],
'Adding roots is different from multiplying roots. √2 + √3 does not become √5.',
'Conjugates are partners with the same terms and the opposite middle sign. Their product removes the radical cross terms.',[
('Simplify √12 + √27.',['√39','5√3','13√3','3√5'],1,'√12 = 2√3 and √27 = 3√3, so the sum is 5√3.'),
('Simplify (√5 + 2)(√5 − 2).',['1','9','√21','−1'],0,'This is a difference of squares: 5 − 4 = 1.'),
('Rationalize 3/√3.',['3√3','1/3','√3','√3/3'],2,'Multiply top and bottom by √3: 3√3/3 = √3.')])
add(1,'right-triangles','Right triangles & exact distance','geo-triangle',[
('Find the side across from the square corner','The longest side is across from the 90° corner. Call it c. Then a² + b² = c².','The Pythagorean theorem applies to right triangles: a² + b² = c². The hypotenuse c is opposite the right angle; a and b are the legs.','In a Euclidean right triangle, the sum of the squares of the leg lengths equals the square of the hypotenuse. Identify c from the right-angle mark, not the drawing’s orientation.'),
('Add to find the long side; subtract for a leg','Legs 6 and 8 give c² = 36 + 64 = 100. So c = 10. If c is given, subtract the other leg’s square.','With legs 6 and 8, c = √(36 + 64) = 10. With hypotenuse 10 and one leg 6, the other is √(100 − 36) = 8. Lengths are positive.','Solve for the required squared length before taking the principal root. Reject algebraic roots that produce nonpositive side lengths. For a square of side s, diagonal d = s√2 for s > 0.'),
('Coordinates hide a right triangle','From (1,2) to (4,6), go 3 across and 4 up. The straight distance is √(3² + 4²) = 5.','Horizontal and vertical changes form the legs of a right triangle. Distance = √((x₂ − x₁)² + (y₂ − y₁)²). Keep an exact radical unless rounding is requested.','The distance formula follows from the Pythagorean theorem using perpendicular coordinate changes. Reversing both endpoint orders leaves the squared differences unchanged.')],
'Never use a² + b² = c² on a triangle unless it is a right triangle. c must be the hypotenuse.',
'A square tile with side 5 has diagonal 5√2, not 10: the diagonal cuts a right triangle across the tile.',[
('A right triangle has legs 5 and 12. Its hypotenuse is…',['7','13','17','√119'],1,'c = √(25 + 144) = √169 = 13.'),
('Hypotenuse 13, one leg 5. Find the other leg.',['18','√194','8','12'],3,'The missing leg is √(13² − 5²) = √144 = 12.'),
('Distance from (−1,1) to (2,5)?',['5','7','√7','25'],0,'The changes are 3 and 4, so distance = √(9 + 16) = 5.')])
add(2,'factoring','Quadratics: factor & solve','geo-quadratic',[
('Give the equation a zero side','Move everything to one side so the other side is zero. Then look for multiplication hiding in the expression.','Write the quadratic in standard form ax² + bx + c = 0, with a ≠ 0. Check for a greatest common factor before factoring further.','Standard form makes coefficients and factor structure visible. An equivalent equation may be obtained by adding, subtracting, or dividing both sides by a nonzero constant.'),
('A zero product gives choices','If two things multiply to zero, at least one must be zero. For (x − 2)(x + 3) = 0, x is 2 or −3.','The zero-product property says AB = 0 implies A = 0 or B = 0. So x² + x − 6 = (x + 3)(x − 2) = 0 has solutions −3 and 2.','After factoring completely, set each variable factor equal to zero and solve. The zero-product property applies to products equal to zero, not sums or products equal to another number.'),
('Check the original equation','Put each answer back into the starting equation. Do both sides match? Then it works.','Substitute each candidate solution into the original equation. Do not lose a solution by dividing by x: x(x − 4) = 0 has both x = 0 and x = 4.','Verification checks the original relationship and any restrictions from a context. A quadratic can have two, one, or no real roots; repeated factors yield a repeated root.')],
'You cannot set each factor equal to zero until the product itself equals zero.',
'A rectangle area equation can become a quadratic. Keep only solutions that give positive physical dimensions.',[
('Solve x² − 9 = 0.',['x = 9 only','x = 3 only','x = −3 or 3','x = −9 or 9'],2,'(x − 3)(x + 3) = 0 gives x = 3 or −3.'),
('Solve x(x − 5) = 0.',['0 and 5','5 only','0 and −5','−5 only'],0,'Either x = 0 or x − 5 = 0. Dividing by x would lose the zero solution.'),
('Before using the zero-product property, you need…',['A positive leading coefficient','A product equal to zero','A linear equation','A decimal answer'],1,'The property requires a product equal to zero.')])
add(2,'formula','The quadratic formula','geo-quadratic',[
('Read a, b, and c with their signs','In 2x² − 3x − 5 = 0, a = 2, b = −3, c = −5. Keep the minus signs attached.','First write ax² + bx + c = 0. The quadratic formula is x = (−b ± √(b² − 4ac))/(2a). Use parentheses when substituting negatives.','For a ≠ 0, the formula solves any quadratic over the complex numbers; here we focus on real roots. Coefficients must be identified from standard form, including their signs.'),
('The plus-or-minus makes two paths','Try the plus sign once and the minus sign once. Both use the whole bottom number, 2a.','For x² − 2x − 3 = 0, x = (2 ± √16)/2 = (2 ± 4)/2, giving 3 and −1. The entire numerator is divided by 2a.','Evaluate the discriminant first, simplify its square root, then reduce the full fraction. If the discriminant is zero, the two formula branches coincide.'),
('The number under the root is a clue','b² − 4ac tells how many real answers there are. Positive: two. Zero: one repeated. Negative: none.','The discriminant D = b² − 4ac determines real-root count. D > 0 gives two distinct real roots; D = 0 gives one repeated real root; D < 0 gives no real roots.','For real coefficients, D classifies the real roots. With integer coefficients, a positive perfect-square discriminant produces rational roots; a positive nonsquare discriminant produces irrational roots.')],
'The denominator is 2a, not just 2. Squaring a negative b requires parentheses.',
'The graph crosses the x-axis twice, touches it once, or misses it according to the discriminant.',[
('For 3x² − 7x + 2 = 0, b is…',['7','−7','2','3'],1,'The coefficient of x is −7, including its sign.'),
('A discriminant of −12 means…',['Two real roots','One repeated real root','No real roots','Twelve real roots'],2,'A negative number has no real square root, so the quadratic has no real solutions.'),
('Solve x² − 2x − 3 = 0.',['−3 and 1','3 and −1','2 and 3','−2 and −3'],1,'The formula gives (2 ± 4)/2, so x = 3 or −1.')])
add(2,'complete-square','Completing the square','geo-quadratic',[
('Make the x² coefficient one','If a number sits before x², divide every term by it first. Move the plain number to the other side.','To complete the square, divide by the leading coefficient if needed, then move the constant. Start with x² + bx = k.','For ax² + bx + c = 0 with a ≠ 0, dividing by a normalizes the quadratic term. Isolate the variable terms before forming a perfect-square trinomial.'),
('Half, then square, then both sides','For x² + 6x, half of 6 is 3. Square 3 to get 9. Add 9 to BOTH sides.','Add (b/2)² to both sides of x² + bx = k. Then x² + bx + (b/2)² = (x + b/2)². Keeping both sides balanced preserves equality.','The identity (x + h)² = x² + 2hx + h² explains the method: h = b/2 after normalization. Fractional values of h are allowed.'),
('Finish with both square-root choices','x² + 6x = 7 becomes (x + 3)² = 16. So x + 3 is 4 or −4. x is 1 or −7.','After forming a square, use ± when taking square roots to solve the equation. (x + 3)² = 16 gives x = −3 ± 4, or 1 and −7.','Solve the resulting equation using the square-root property and isolate x. The principal radical √16 is 4, but an equation u² = 16 has u = ±4.')],
'Adding to just one side changes the equation. Taking a square root without ± can lose a solution.',
'Completing a square turns an awkward quadratic into one squared expression you already know how to undo.',[
('What completes x² + 10x + ___?',['5','10','20','25'],3,'Half of 10 is 5, and 5² = 25.'),
('Solve (x + 2)² = 9.',['1 and −5','1 only','5 and −1','−5 only'],0,'x + 2 = ±3, so x = 1 or −5.'),
('To complete x² + 4x = 12, add…',['4 to the left only','2 to both sides','4 to both sides','16 to both sides'],2,'Half of 4 is 2; its square is 4. Add 4 to both sides.')])
add(2,'systems','Systems: where equations agree','geo-system',[
('One answer must fit both rules','A system is two rules at once. Its answer must make BOTH equations true. On a graph, look where they meet.','A solution to a two-variable system is an ordered pair (x,y) satisfying every equation. Graphically it is an intersection point.','The solution set is the intersection of the equations’ solution sets. A linear–quadratic system can have zero, one, or two real intersection points.'),
('Substitute or eliminate','If y = x + 1, use x + 1 wherever you see y in the other equation. Or add equations so one letter cancels.','Substitution replaces a variable with an equal expression. Elimination multiplies equations as needed and adds or subtracts them to cancel a variable. Solve, then find the other coordinate.','Equivalent substitution and linear combinations reduce the number of unknowns. In a linear–quadratic system, substitution often produces a quadratic; each real root must be paired with its matching y-value.'),
('Translate a rectangle story','A rectangle with length L and width W has area LW and perimeter 2L + 2W. These give two rules for the same shape.','For area 24 and perimeter 20: LW = 24 and L + W = 10. Substitute W = 10 − L to get L(10 − L) = 24. The dimensions are 4 and 6.','Use consistent units and positive dimensions. The roots 4 and 6 of L² − 10L + 24 = 0 describe the same rectangle when length and width labels are exchanged.')],
'An x-value alone is not a full ordered-pair solution. Check both coordinates in both original equations.',
'For y = x² and y = x + 2, intersections satisfy x² = x + 2, giving (−1,1) and (2,4).',[
('Solve y = x + 1 and x + y = 7.',['(4,3)','(3,4)','(2,5)','(7,8)'],1,'Substitute: x + x + 1 = 7, so x = 3 and y = 4.'),
('y = x² and y = 4 have which intersections?',['(2,4) only','(−2,4) only','(−2,4) and (2,4)','(4,2) and (4,−2)'],2,'x² = 4 gives x = ±2; both have y = 4.'),
('Area 24, perimeter 20: rectangle side lengths?',['2 and 12','3 and 8','4 and 6','5 and 5'],2,'4 × 6 = 24 and 2(4 + 6) = 20.')])
add(3,'points','Points, segments & rays','geo-segment',[
('Know what stops and what keeps going','A point is a location. A segment stops at two ends. A ray starts at one end and keeps going. A line keeps going both ways.','A point has no dimensions. A line extends infinitely in both directions. A segment has two endpoints. A ray has one endpoint and extends infinitely in one direction.','Points identify positions; lines and rays have infinite extent, while segments have finite length. Name a ray with its endpoint first: ray AB begins at A and passes through B.'),
('Read coordinates in order','For (−2,3), go left 2, then up 3. Always x first, y second.','In (x,y), x gives horizontal position and y vertical position. Quadrants I, II, III, IV have signs (+,+), (−,+), (−,−), (+,−). Points on axes are not in quadrants.','The Cartesian plane uses perpendicular x- and y-axes. Ordered pairs locate points uniquely; reversing coordinates generally gives a different point.'),
('Pieces make the whole','If B is between A and C, add AB and BC to get AC. If AC is 15 and AB is 6, BC is 9.','Segment addition: if B lies between A and C, AB + BC = AC. For AB = 2x, BC = x + 3, AC = 18, solve 3x + 3 = 18, so x = 5.','Between-ness is required for this segment-addition equation. Segment notation denotes the geometric set; AB without a segment bar commonly denotes its length. Copy a length with a compass by transferring the endpoint distance.')],
'Ray AB and ray BA generally point in different directions. Do not add pieces unless the diagram or text establishes their positions.',
'A trip from A to C through a point B on the segment has two lengths that add to the full distance.',[
('Which object has exactly one endpoint?',['Line','Point','Ray','Segment'],2,'A ray begins at one endpoint and extends without end in one direction.'),
('Which quadrant contains (−4,2)?',['I','II','III','IV'],1,'Negative x and positive y put the point in quadrant II.'),
('B is between A and C. AB = 7, AC = 19. BC = ?',['26','12','7','19'],1,'AB + BC = AC, so BC = 19 − 7 = 12.')])
add(3,'midpoints','Midpoints & segment bisectors','geo-midpoint',[
('A midpoint makes equal halves','A midpoint is the exact middle of a segment. The two little lengths are equal.','If M is the midpoint of AB, AM = MB and AB = 2AM. A segment bisector is a line, ray, or segment passing through that midpoint.','A midpoint partitions a segment into two congruent segments. A segment bisector need not be perpendicular; passing through the midpoint is the defining condition.'),
('Average x, then average y','Between (0,2) and (6,8), the middle x is 3 and the middle y is 5. The midpoint is (3,5).','M = ((x₁ + x₂)/2, (y₁ + y₂)/2). For a missing endpoint, double the midpoint coordinates and subtract the known endpoint coordinates.','The midpoint formula averages coordinate components independently. If M is the midpoint of AB, then B = (2Mₓ − Aₓ, 2Mᵧ − Aᵧ).'),
('Construct the middle with equal arcs','Open a compass more than halfway across the segment. Draw equal-size arcs from both ends. Join their two crossing points.','Use the same compass radius, greater than half the segment length, from both endpoints. Join the two arc intersections. This line crosses the segment at its midpoint and at 90°.','Equal-radius intersecting circles centered at A and B determine two points equidistant from A and B. Their connecting line is the perpendicular bisector. A radius at or below half the segment length does not give two distinct intersections.')],
'A segment bisector alone guarantees equal halves, not a 90° angle.',
'If one half is 3x + 1 and the other is x + 9, set them equal: x = 4, so each half is 13.',[
('Midpoint of (−2,4) and (6,0)?',['(4,4)','(2,2)','(2,4)','(−4,2)'],1,'Average x: (−2 + 6)/2 = 2; average y: (4 + 0)/2 = 2.'),
('M(3,5) is midpoint; A(1,2). Find B.',['(2,3)','(4,7)','(5,8)','(6,10)'],2,'B = (2·3 − 1, 2·5 − 2) = (5,8).'),
('Every segment bisector must…',['Be vertical','Make a right angle','Pass through the midpoint','Be a full line'],2,'A bisector passes through the midpoint; perpendicularity is an extra condition.')])
add(3,'slope','Slope: rise over run','geo-slope',[
('Slope measures steepness and direction','Slope tells how much y changes when x changes. Go up 2 and right 1: slope is 2.','m = (y₂ − y₁)/(x₂ − x₁), when x₂ ≠ x₁. Keep endpoint order consistent. Positive slopes rise left to right; negative slopes fall.','Slope is the ratio of vertical to horizontal coordinate change. Reversing both subtraction orders gives the same ratio; reversing only one changes the sign incorrectly.'),
('Horizontal is zero; vertical is undefined','A flat line has no rise, so slope is 0. A vertical line has no run; you cannot divide by 0.','A horizontal line has equation y = k and slope 0. A vertical line has equation x = k and undefined slope. Remember HOY / VUX.','For horizontal distinct points, Δy = 0 and Δx ≠ 0, giving m = 0. Vertical distinct points have Δx = 0, so their slope is undefined rather than infinite.'),
('Check whether points share a line','Points are collinear if one straight line goes through them. Compare slopes from the same point.','For distinct points, equal slopes from a shared point show collinearity, provided the slopes exist. If all x-coordinates match, the points lie on one vertical line.','Collinear points lie on one line. Handle undefined slopes explicitly: common x-coordinates establish a vertical line, while equality of two defined slopes from a common point establishes nonvertical collinearity.')],
'Zero slope and undefined slope are different. A vertical line is x = a number, not y = a number.',
'A ramp rising 2 units across a horizontal run of 5 has slope 2/5.',[
('Slope through (1,2) and (3,8)?',['1/3','3','6','−3'],1,'m = (8 − 2)/(3 − 1) = 6/2 = 3.'),
('What is the slope of x = −2?',['−2','0','Undefined','2'],2,'x = −2 is vertical, so its horizontal change is zero.'),
('A horizontal line through (4,−3) is…',['x = 4','y = 4','x = −3','y = −3'],3,'All points on the horizontal line have the same y-coordinate, −3.')])
add(3,'line-equations','Build a line equation','geo-slope',[
('Use y = mx + b','m is the slope. b is where the line hits the y-axis. For slope 2 and b = 3, write y = 2x + 3.','In y = mx + b, m is slope and (0,b) is the y-intercept. This form describes nonvertical lines. A vertical line is x = k.','Slope-intercept form parameterizes nonvertical lines by slope and y-intercept. Horizontal lines fit with m = 0; vertical lines require a separate equation.'),
('Use a point to find b','Slope 3 through (2,7)? Put 2 and 7 into y = 3x + b. Then 7 = 6 + b, so b = 1.','Find m, substitute a given point into y = mx + b, solve for b, then write the equation using variables x and y. With m = 3 through (2,7), y = 3x + 1.','Given two points, first compute their slope unless the x-coordinates match. Then solve b = y₁ − mx₁. Equivalent point-slope form is y − y₁ = m(x − x₁).'),
('Check the finished rule','Put the given point into your final equation. The two sides should match.','For y = 3x + 1, the point (2,7) works because 7 = 3(2) + 1. With two given points, check both; also check that the slope matches.','Verification checks both incidence and direction. A line through two distinct points is unique; a point and a specified slope likewise determine one line.')],
'The b is a y-intercept, not whichever y-value appears in the given point.',
'Through (1,4) and (3,8), slope is 2 and b is 2, giving y = 2x + 2.',[
('Slope 2 through (3,7). Equation?',['y = 2x + 7','y = 2x + 1','y = 3x + 2','x = 3'],1,'7 = 2(3) + b gives b = 1.'),
('Vertical line through (5,−2)?',['y = −2','y = 5','x = 5','x = −2'],2,'A vertical line keeps x fixed, so x = 5.'),
('y = −3x + 4 has y-intercept…',['(0,4)','(4,0)','(0,−3)','(−3,0)'],0,'Set x = 0: y = 4.')])
add(4,'angles','Angles & equal halves','geo-angle',[
('Name and measure an angle','Two rays with the same starting point make an angle. In ∠ABC, B is the corner.','An angle is formed by two rays sharing a vertex. The vertex is the middle letter in a three-letter name. Acute: 0° < θ < 90°; right: 90°; obtuse: 90° < θ < 180°; straight: 180°.','Angle names place the vertex between points on the two rays. A lone vertex letter is sufficient only when it unambiguously names the angle. Adjacent component measures add to the whole angle.'),
('90, 180, or 360?','Two angles adding to 90° are complementary. Adding to 180° makes them supplementary. A full turn is 360°.','Complementary angles sum to 90°; supplementary angles sum to 180°. A linear pair forms a straight angle, so its angles sum to 180°. Angles around one point sum to 360°.','Complementary and supplementary relationships concern sums, not necessarily adjacency. Vertical angles are congruent. Adjacent angles forming a straight line are supplementary.'),
('Bisect means two equal angles','A bisector splits an angle right down the middle. Half of 110° is 55°.','An angle bisector divides an angle into two congruent angles. For halves 3x + 5 and 5x − 15, equate them: x = 10, so each half is 35° and the whole is 70°.','A ray bisecting an angle creates equal angle measures, unlike an arbitrary interior ray. For a compass construction, mark equal distances on both rays, draw equal intersecting arcs from those marks, then connect the vertex to their intersection.')],
'A picture that looks like equal angles is not proof. Use markings, a stated bisector, or a known relationship.',
'For adjacent angles 28° and 47°, the whole is 75°. Its bisector would make two 37.5° angles.',[
('In ∠PQR, the vertex is…',['P','Q','R','Any letter'],1,'The middle letter Q names the shared endpoint.'),
('An angle complements 34°. Its measure is…',['146°','56°','34°','66°'],1,'Complementary angles sum to 90°: 90 − 34 = 56.'),
('A bisector divides a 126° angle into…',['Two 63° angles','Two 126° angles','36° and 90°','Two 62° angles'],0,'Bisect means two congruent halves, and 126/2 = 63.')])
add(4,'parallel','Parallel lines & angle pairs','geo-parallel',[
('A transversal crosses two lines','A transversal is a line cutting across other lines. Look at where each angle sits, not how big it looks.','For two distinct coplanar parallel lines cut by a transversal, corresponding, alternate interior, and alternate exterior angles are congruent. Same-side interior angles are supplementary.','Parallel lines in a plane do not intersect. The packet also treats coincident lines as having the same direction; here the usual distinct-line parallel-angle theorems use two separate parallel lines.'),
('Spot matching or adding pairs','Corresponding angles sit in matching corners. Alternate interior angles are inside the lines on opposite sides of the crossing line.','Corresponding angles occupy the same relative position at each intersection. Alternate interior pairs are between the lines on opposite sides of the transversal; alternate exterior pairs are outside on opposite sides.','Use position to identify the relationship before writing an equation. Parallelism establishes congruence for corresponding and alternate pairs; same-side interior measures sum to 180°.'),
('Turn the relationship into an equation','If matching angles are 2x + 10 and 70, set 2x + 10 = 70. If they add to 180, use a sum instead.','For parallel lines, corresponding angles 2x + 10 and 70 yield x = 30. Same-side interior angles 2x and 3x yield 5x = 180, so x = 36.','The relationship determines equality versus supplementation. Check the resulting angle measures against both the given expressions and the required total. Copying a corresponding angle through an external point constructs a parallel line.')],
'The special equal-angle rules require parallel lines. A transversal alone is not enough.',
'If one angle in the parallel-line model is 65°, all the acute angles are 65° and all the obtuse angles are 115°.',[
('Parallel lines: an alternate interior partner of 68° measures…',['112°','22°','68°','136°'],2,'Alternate interior angles are congruent when the lines are parallel.'),
('Parallel lines: same-side interior angles are 3x and 2x. x = ?',['18','36','45','90'],1,'3x + 2x = 180 gives x = 36.'),
('Before using corresponding-angle congruence here, confirm…',['The lines are parallel','The angles look equal','The transversal is horizontal','All angles are acute'],0,'Parallel lines guarantee corresponding angles are congruent.')])
add(4,'perpendicular','Parallel & perpendicular equations','geo-lines',[
('Parallel lines share direction','Parallel nonvertical lines have the same slope. Different heights can still mean the same steepness.','Distinct nonvertical parallel lines have equal slopes and different intercepts. Distinct vertical lines are parallel to each other.','Equal finite slopes give parallel or coincident lines. Distinct intercepts distinguish separate lines. Vertical parallel lines have undefined slopes, handled separately.'),
('Perpendicular lines make 90°','For a nonzero slope, flip its fraction and change its sign. A slope of 2/3 pairs with −3/2.','Nonvertical perpendicular lines have slopes whose product is −1. Use the negative reciprocal. Horizontal and vertical lines are perpendicular to each other.','For nonzero finite m, a perpendicular slope is −1/m. The zero-slope case has a vertical perpendicular and cannot be handled by dividing by zero.'),
('Find the new line through a point','Choose the needed slope first. Then use your point to find b in y = mx + b.','A line perpendicular to y = 2x + 1 through (0,3) has slope −1/2 and intercept 3: y = −x/2 + 3. For a vertical answer, use x = k.','To construct a perpendicular through a point, identify two equal-distance intersections on the original line, then use equal arcs from those intersections to locate a second point on the perpendicular.')],
'Changing only the sign is not enough: the perpendicular slope to 2 is −1/2, not −2.',
'A line parallel to y = 3x − 4 through (2,1) is y = 3x − 5.',[
('Perpendicular slope to 3/4?',['−3/4','4/3','−4/3','3/4'],2,'The negative reciprocal is −4/3; their product is −1.'),
('Parallel to y = −2x + 5 through (1,1)?',['y = 2x − 1','y = −2x + 3','y = x + 1','x = 1'],1,'Use slope −2. Then 1 = −2(1) + b, so b = 3.'),
('A line perpendicular to a horizontal line is…',['Horizontal','Vertical','Always slope 1','Always slope −1'],1,'A vertical line meets a horizontal line at 90°.')])
add(4,'centers','Bisectors, incenters & circumcenters','geo-centers',[
('A perpendicular bisector does two jobs','It cuts a segment in half AND makes a square corner. Any point on it is equally far from the segment’s two ends.','A perpendicular bisector passes through a segment’s midpoint at 90°. Every point on it is equidistant from the endpoints. To find its equation, combine the midpoint with a perpendicular slope.','The perpendicular bisector is the locus of points equidistant from the two endpoints. Coordinate construction uses the midpoint and negative reciprocal slope, with horizontal/vertical exceptions.'),
('Incenter: equal distance to sides','A triangle’s angle bisectors meet at the incenter. It is inside the triangle. A circle centered there can touch all three sides.','The incenter is the common intersection of the triangle’s three internal angle bisectors. It is equidistant from the sides and is the center of the inscribed circle. Distance to a side is measured perpendicularly.','Two internal angle bisectors suffice to locate the incenter; the third passes through the same point. Use a perpendicular radius to a side to set the incircle radius, not the distance to a vertex.'),
('Circumcenter: equal distance to corners','A triangle’s side perpendicular bisectors meet at the circumcenter. A circle centered there passes through all three corners.','The circumcenter is the intersection of the side perpendicular bisectors. It is equidistant from the three vertices and is the center of the circumscribed circle. It can lie outside the triangle.','The circumcenter is inside an acute triangle, at the hypotenuse midpoint of a right triangle, and outside an obtuse triangle. Construct two side perpendicular bisectors, then use the distance to any vertex as the circumradius.')],
'Incenter uses angle bisectors and distances to sides. Circumcenter uses perpendicular bisectors and distances to vertices.',
'For a segment from (0,0) to (4,0), the perpendicular bisector is x = 2; every point on it is equally far from both endpoints.',[
('Which point is equidistant from all three triangle sides?',['Circumcenter','Incenter','Any vertex','Any midpoint'],1,'The incenter lies on the angle bisectors and is equidistant from the sides.'),
('A circumcircle passes through…',['All three vertices','All three side midpoints','Only one vertex','The incenter only'],0,'The circumcenter is equidistant from the vertices, so its circle passes through all three.'),
('Perpendicular bisector of (0,0) to (6,0)?',['y = 3','x = 6','y = 0','x = 3'],3,'The midpoint is (3,0); the segment is horizontal, so its perpendicular bisector is vertical, x = 3.')])
add(4,'angle-strategy','Unknown angles: build a plan','geo-angle',[
('Start with one certain relationship','Mark what you know. A straight line totals 180°. A triangle totals 180°. A full turn totals 360°.','Identify the smallest useful relationship: linear pair, vertical angles, triangle sum, full turn, bisector, or parallel-line angle pair. Mark known values before solving.','Use the givens and established theorems to justify each equation. Diagram appearance alone does not establish parallelism, perpendicularity, or congruence.'),
('Name the unknown and solve','If a triangle has 50° and 60°, the last angle is 180 − 50 − 60 = 70°.','For triangle angles x, 2x, and 3x, write x + 2x + 3x = 180. Then x = 30°, giving angles 30°, 60°, and 90°.','Translate the angle relationship into an algebraic equation, solve it, then evaluate every requested angle expression. An algebraic variable is not always itself the angle measure.'),
('Add a helpful line when it unlocks a clue','Sometimes drawing an extra line makes a familiar angle pair appear. Add it for a reason and say what it helps you use.','An auxiliary line is a line you add to a diagram to make useful relationships visible. A parallel through a vertex can reveal alternate interior or corresponding angles. Explain the reason for adding it.','An auxiliary construction must have a specified property, such as passing through a point parallel to a given line. Use that property to justify subsequent equalities, then check all angle sums and constraints.')],
'If the problem asks for an angle written 3x + 5, finding x is only the first step. Substitute to finish.',
'If a triangle’s angles are x + 10, 2x, and 80°, then 3x + 90 = 180, so x = 30° and the angles are 40°, 60°, 80°.',[
('Triangle angles 45°, 65°, and θ. θ = ?',['70°','80°','110°','250°'],0,'Triangle angles sum to 180°: 180 − 45 − 65 = 70.'),
('Angles around a point total…',['90°','180°','270°','360°'],3,'One full turn is 360°.'),
('x = 20 and an angle is 3x + 5 degrees. The angle is…',['20°','60°','65°','25°'],2,'Substitute x = 20: 3(20) + 5 = 65°.')])
# Copying an angle is a distinct construction in the supplied angle packet.
p=('Copy an angle with a compass','Draw a new starting ray. Use equal-size arcs at the old and new corners. Copy the distance between the old arc marks to the new arc, then draw the new ray.','Draw a new base ray. From the original vertex, draw an arc crossing both angle rays. With the same radius, draw an arc from the new vertex. Transfer the distance between the original two arc intersections onto the new arc, then join the new vertex to that mark.','Preserve the original vertex-to-arc radius in the new construction. Transfer the chord length between the original ray–arc intersections to the new arc. The resulting triangle has three matching side lengths, so the constructed angle is congruent to the original.')
t=next(t for t in T if t['id']=='geo-angles');i=len(t['parts']);t['parts'].append([p[0],p[2]])
for k,n in [('easy',1),('medium',2),('expert',3)]:
 if k!='medium':R[t['id']][k]['parts'].append([p[0],p[n]])
C.append({'topic':t['id'],'section':i,'front':p[0]+' — explain it in your own words.','back':p[2]})
# Align navigation with every printed day, keeping the four uploaded packet units.
old={t['id']:t for t in T}
OR=json.loads(json.dumps(R))
new=[]
def day(unit,num,id,title,source,indices,model=None,constructions=None):
 src=old['geo-'+source]; tid='geo-'+id
 versions={k:{**OR[src['id']][k],'parts':[OR[src['id']][k]['parts'][i][:] for i in indices]} for k in ['easy','medium','expert']}
 t={**src,'id':tid,'title':title,'unit':unit,'day':num,'group':f'Unit {unit} · Day {num}','model':model or src['model'],'constructions':constructions or [],'parts':versions['medium']['parts']}
 new.append(t);R[tid]=versions
 return t
def part(t,title,easy,medium,expert):
 for k,text in [('easy',easy),('medium',medium),('expert',expert)]:R[t['id']][k]['parts'].append([title,text])
 t['parts']=R[t['id']]['medium']['parts']
day(1,1,'radicals','Simplifying Radicals','radicals',[0,1,2])
day(1,2,'radical-operations','Adding and Subtracting Radicals','radical-operations',[0])
t=day(1,3,'radical-products','Multiplying and Dividing Radicals','radical-operations',[1])
part(t,'Divide and simplify','For √48 ÷ √3, divide inside the roots: √(48/3) = √16 = 4. The denominator cannot be zero.','For a ≥ 0 and b > 0, √a/√b = √(a/b). Simplify the fraction, then the radical. For example, √48/√3 = 4.','The quotient property requires a nonnegative numerator radicand and positive denominator radicand in real-number work. Apply distribution to polynomial products, and simplify all resulting radicals.')
day(1,4,'rationalize','Rationalizing Denominators','radical-operations',[2])
day(1,5,'right-triangles','Pythagorean Theorem','right-triangles',[0,1,2])
for num,id,title in [(1,'factoring','Solving Quadratics by Factoring'),(2,'formula','The Quadratic Formula'),(3,'complete-square','Completing the Square'),(4,'systems','Systems of Equations')]:day(2,num,id,title,id,[0,1,2])
day(3,1,'points','Points, Lines, Segments and Rays','points',[0,1,2],constructions=['copy-segment'])
day(3,2,'midpoints','Midpoint','midpoints',[0,1,2],constructions=['midpoint'])
t=day(3,3,'bisectors','Segment Bisectors','midpoints',[0],model='geo-midpoint')
part(t,'Turn congruent halves into an equation','If a bisector creates lengths 4x − 1 and 2x + 7, set them equal. Then 2x = 8, so x = 4 and each half is 15.','A segment bisector passes through the midpoint, so the two halves are congruent. Set their length expressions equal, solve, and substitute to find each requested length.','A bisector establishes a midpoint and equality of the two subsegment lengths. Use these facts with segment addition to relate a half-length to the whole. A general segment bisector need not be perpendicular.')
part(t,'Check what is actually bisected','Look for the segment named in the problem. A line crossing two segments might cut only one of them in half.','State which segment is bisected and identify its midpoint. Do not assume that both intersecting segments bisect each other without evidence.','Incidence at a common point does not establish reciprocal bisection. Distinguish the bisecting object from the segment whose two parts are congruent.')
day(3,4,'slope','Slope','slope',[0,1,2])
day(3,5,'line-equations','Writing the Equation of a Line','line-equations',[0,1,2])
day(4,1,'angles','Types of Angles','angles',[0,1,3],constructions=['copy-angle'])
t=day(4,2,'angle-bisector','Angle Bisector','angles',[2],constructions=['angle-bisector','incircle'])
part(t,*['Incenter and incircle']+[OR['geo-centers'][k]['parts'][1][1] for k in ['easy','medium','expert']])
day(4,3,'parallel','Parallel Lines','parallel',[0,1,2])
t=day(4,4,'perpendicular','Constructing Parallel and Perpendicular Lines','perpendicular',[0,1,2],constructions=['parallel-corresponding','parallel-alternate','perpendicular-on','perpendicular-off'])
t=day(4,5,'centers','Perpendicular Bisector','centers',[0],constructions=['perpendicular-bisector'])
part(t,'Write its equation','Find the segment midpoint first. Use a slope perpendicular to the segment and make the new line pass through that midpoint.','For A(0,0) and B(4,2), midpoint M = (2,1), segment slope = 1/2, and perpendicular slope = −2. Substituting M gives y = −2x + 5.','Compute M = ((x₁+x₂)/2,(y₁+y₂)/2), then use the perpendicular direction through M. A horizontal segment has a vertical bisector; a vertical segment has a horizontal bisector.')
t=day(4,6,'circumcenter','Circumcenter','centers',[2],constructions=['circumcircle'])
part(t,'Find it with two perpendicular bisectors','Construct the perpendicular bisectors of two sides. Their intersection is the circumcenter. Keep the compass centered there and open it to any vertex to draw the circle.','Two side perpendicular bisectors locate the circumcenter. Use the distance from that point to any vertex as the radius of the circumcircle. All three vertices must lie on the circle.','Perpendicular-bisector intersections are equidistant from the triangle vertices. Two bisectors suffice; the third is concurrent. For coordinate problems, solve the equations of two perpendicular bisectors.')
day(4,7,'angle-strategy','Unknown Angle Problems','angle-strategy',[0,1,2])
T=new
# Plain, age-appropriate language: keep the mathematical terms and remove personification.
R['geo-radicals']['easy']['parts'][0][1]='A square root reverses squaring. Since 5 × 5 = 25, √25 = 5. The radical symbol gives the nonnegative root. Solving x² = 25 is different: both 5 and −5 work.'
for t in T:
 for k in ['easy','medium','expert']:
  for p in R[t['id']][k]['parts']:
   p[0]=p[0].replace('What does a root mean?','Square roots and number types').replace('Pull out a perfect square','Simplify using a perfect-square factor').replace('Variables need a small safety check','Variable radicals and absolute value').replace('Only matching roots combine','Like radicals').replace('Clear a root from the bottom','Rationalizing the denominator').replace('Find the side across from the square corner','Identify the hypotenuse')
 t['parts']=R[t['id']]['medium']['parts'];t['desc']=R[t['id']]['medium']['desc']
# Each daily lesson teaches a method, a worked application, and a check.
t=next(t for t in T if t['id']=='geo-radical-operations')
part(t,'Simplify before combining','√8 + √18 = 2√2 + 3√2 = 5√2. Simplifying first reveals that the terms are like radicals.','Simplify every radical before combining terms. For √8 + √18, extract square factors to get 2√2 + 3√2 = 5√2.','Rewrite radicals in simplest form before identifying like radical factors. Combine only coefficients of matching simplified radicals.')
part(t,'Handle subtraction carefully','For 4√3 − (√3 + 2√5), subtract both terms inside the parentheses. The result is 3√3 − 2√5.','Distribute a subtraction sign to every term it affects. 4√3 − (√3 + 2√5) = 4√3 − √3 − 2√5 = 3√3 − 2√5.','Subtraction is addition of the opposite expression. Apply the negative sign across all terms, then combine like radicals; unlike radicals remain separate.')
t=next(t for t in T if t['id']=='geo-radical-products')
part(t,'Multiply two binomials','(√3 + 2)(√3 − 2) = 3 − 2√3 + 2√3 − 4 = −1. Multiply all four pairs, then combine terms.','Use distribution for every pair of terms. (√3 + 2)(√3 − 2) simplifies to 3 − 4 = −1 because the middle terms cancel.','The product of conjugates is a difference of squares. Distribution gives (a + b)(a − b) = a² − b², including when one or both terms are radicals.')
t=next(t for t in T if t['id']=='geo-rationalize')
part(t,'A single radical in the denominator','For 2/√3, multiply the numerator and denominator by √3. The result is 2√3/3.','Multiply top and bottom by a radical that makes the denominator rational: 2/√3 = 2√3/3. This multiplies the fraction by 1.','Choose a radical factor that converts the denominator radicand to a perfect square. Apply the same nonzero factor to numerator and denominator to preserve equivalence.')
part(t,'A binomial in the denominator','For 1/(√5 + 1), multiply the numerator and denominator by √5 − 1. The denominator becomes 5 − 1 = 4.','Use the conjugate for a two-term denominator: 1/(√5 + 1) = (√5 − 1)/((√5 + 1)(√5 − 1)) = (√5 − 1)/4.','The conjugate removes the radical cross terms through the difference-of-squares identity. Preserve any original nonzero-denominator restrictions and simplify the resulting fraction.')
t=next(t for t in T if t['id']=='geo-centers')
part(t,'Use equal endpoint distances','P lies on the perpendicular bisector of AB. If PA = 2x + 3 and PB = x + 8, set them equal. Then x = 5 and both distances are 13.','A point on the perpendicular bisector is equidistant from the endpoints. Use PA = PB to solve expressions such as 2x + 3 = x + 8.','Apply the perpendicular-bisector theorem to equate distances from a point on the bisector to the segment endpoints. Distinguish this equality from the equality of the two segment halves.')
# Easy is concise secondary-school language, with the correct terminology retained.
easy_overrides={
'geo-radicals':['A square root reverses squaring. Since 5² = 25, √25 = 5. The radical symbol gives the nonnegative root; solving x² = 25 gives both 5 and −5.','Simplify √72 by factoring 72 as 36 × 2. Since √36 = 6, √72 = 6√2. Use the largest perfect-square factor to reduce the work.','For any real x, √(x²) = |x| because a principal square root cannot be negative. If x is known to be nonnegative, |x| = x.'],
'geo-radical-operations':['Add or subtract radicals only when their simplified radicands match. For example, 3√2 + 4√2 = 7√2. The radicand stays 2.'],
'geo-radical-products':['Multiply the coefficients and multiply the radicands, then simplify. √3 × √12 = √36 = 6. Use distribution when a factor has more than one term.'],
'geo-rationalize':['Rationalizing rewrites a fraction without a radical in its denominator. Multiply the numerator and denominator by the same nonzero expression so the value stays unchanged.'],
'geo-right-triangles':['In a right triangle, the hypotenuse is opposite the 90° angle. The other sides are the legs. The Pythagorean theorem is a² + b² = c², where c is the hypotenuse.','For legs 6 and 8, c² = 36 + 64 = 100, so c = 10. To find a missing leg, subtract the known leg’s square from the hypotenuse’s square before taking the square root.','From (1,2) to (4,6), the horizontal change is 3 and vertical change is 4. These form perpendicular legs, so the distance is √(3² + 4²) = 5.'],
'geo-factoring':['Write the equation with zero on one side and terms in descending powers. Factor out a common factor first, if there is one.','If a product equals zero, at least one factor equals zero. For (x − 2)(x + 3) = 0, solve x − 2 = 0 or x + 3 = 0. The solutions are 2 and −3.','Substitute each solution into the original equation. Do not divide by a variable that could be zero: x(x − 4) = 0 has solutions 0 and 4.'],
'geo-formula':['First write ax² + bx + c = 0. In 2x² − 3x − 5 = 0, a = 2, b = −3, and c = −5. Keep the signs with the coefficients.','Use x = (−b ± √(b² − 4ac))/(2a). Calculate once with + and once with −. Divide the entire numerator by 2a.','The discriminant is b² − 4ac. A positive result gives two real solutions, zero gives one repeated solution, and a negative result gives no real solutions.'],
'geo-complete-square':['If the coefficient of x² is not 1, divide every term by it. Then move the constant term to the other side.','For x² + 6x, half of 6 is 3 and 3² = 9. Add 9 to both sides so the left becomes (x + 3)².','x² + 6x = 7 becomes (x + 3)² = 16. Then x + 3 = ±4, giving x = 1 or x = −7.'],
'geo-systems':['A solution to a system must satisfy both equations. On a graph, the solutions are the intersection points.','For substitution, replace a variable with an equal expression from the other equation. For elimination, combine equations so one variable cancels. Then solve for both coordinates.','For a rectangle, area = LW and perimeter = 2L + 2W. These form two equations for the same dimensions. Keep only positive side lengths.'],
'geo-points':['A point is a location. A line extends in both directions; a segment has two endpoints. A ray has one endpoint and extends in one direction.','In (x,y), x is the horizontal coordinate and y is the vertical coordinate. To plot (−2,3), move left 2 and up 3.','If B lies between A and C, AB + BC = AC. If AC = 15 and AB = 6, then BC = 9. Use a compass to transfer a segment length without measuring it with a ruler.'],
'geo-midpoints':['A midpoint divides a segment into two congruent segments. A segment bisector passes through that midpoint; it does not have to be perpendicular.','Average the x-coordinates and then the y-coordinates. The midpoint of (0,2) and (6,8) is (3,5). To find a missing endpoint, double the midpoint and subtract the known endpoint.','Use equal compass openings greater than half the segment length. Draw intersecting arcs from both endpoints. Connect the two arc intersections to locate the midpoint.'],
'geo-slope':['Slope is the change in y divided by the change in x. A rise of 2 for a run of 1 gives slope 2.','A horizontal line has slope 0 because its vertical change is zero. A vertical line has undefined slope because division by zero is undefined.','Collinear points lie on the same line. Compare slopes using a shared point, or check whether all x-coordinates match for a vertical line.'],
'geo-line-equations':['In y = mx + b, m is the slope and b is the y-intercept. For m = 2 and b = 3, the equation is y = 2x + 3.','For slope 3 through (2,7), substitute into y = 3x + b. Then 7 = 6 + b, so b = 1 and y = 3x + 1.','Substitute the given point into your final equation. With two given points, check both. Handle a vertical line separately as x = a constant.'],
'geo-angles':['An angle is formed by two rays sharing a vertex. In ∠ABC, B is the vertex. Acute angles are below 90°, right angles equal 90°, obtuse angles lie between 90° and 180°, and straight angles equal 180°.','Complementary angles total 90°; supplementary angles total 180°. A full turn is 360°. Opposite angles formed by intersecting lines are vertical angles and are equal.','Draw a new base ray. Use the same-radius arcs at the original and new vertices. Transfer the distance between the original arc marks onto the new arc, then draw the second ray.'],
'geo-angle-bisector':['An angle bisector divides an angle into two congruent angles. Bisecting 110° gives two 55° angles. If the two halves are expressions, set them equal.','A triangle’s internal angle bisectors meet at the incenter. It is inside the triangle and equally distant from its sides. Its circle, the incircle, touches all three sides.'],
'geo-parallel':['A transversal crosses two lines at different points. If those lines are parallel, corresponding and alternate angles are equal; same-side interior angles total 180°.','Corresponding angles occupy matching positions. Alternate interior angles are between the lines and on opposite sides of the transversal.','Choose the relationship before writing an equation. Equal angles 2x + 10 and 70 give 2x + 10 = 70. Same-side interior angles 2x and 3x give 2x + 3x = 180.'],
'geo-perpendicular':['Parallel nonvertical lines have the same slope. Vertical lines are parallel to other distinct vertical lines.','Perpendicular lines meet at 90°. For a nonzero slope, use the negative reciprocal: 2/3 becomes −3/2. A horizontal line is perpendicular to a vertical line.','Choose the parallel or perpendicular slope first. Substitute the given point into y = mx + b to find b. For a vertical line, use x = a constant.'],
'geo-centers':['A perpendicular bisector passes through a segment’s midpoint at 90°. Every point on it is equally far from the two endpoints.'],
'geo-circumcenter':['A triangle’s side perpendicular bisectors meet at the circumcenter. It is equally far from all three vertices. A circle centered there passes through the vertices, and the center can be outside the triangle.'],
'geo-angle-strategy':['Start with a known relationship: a straight angle is 180°, a triangle totals 180°, and a full turn is 360°. Use markings and stated facts, rather than how the diagram looks.','Write an equation using the angle relationship. For triangle angles x, 2x, and 3x, solve 6x = 180. Then x = 30°, so the angles are 30°, 60°, and 90°.','An auxiliary line is an extra line added for a specific reason. For example, drawing a parallel through a vertex can reveal equal alternate interior angles. Explain why the added line helps.']}
for t in T:
 for i,text in enumerate(easy_overrides.get(t['id'],[])):R[t['id']]['easy']['parts'][i][1]=text
 t['parts']=R[t['id']]['medium']['parts']
examples={
'geo-radicals':'√98 = √(49 × 2) = 7√2. The factor 49 is a perfect square.',
'geo-radical-operations':'√20 + √45 = 2√5 + 3√5 = 5√5. Simplify before combining coefficients.',
'geo-radical-products':'√2(3 + √2) = 3√2 + 2. Multiply √2 by both terms inside the parentheses.',
'geo-rationalize':'2/√3 = (2√3)/(√3 × √3) = 2√3/3. Multiplying top and bottom by √3 preserves the value.',
'geo-right-triangles':'For a square with side 5, d² = 5² + 5² = 50, so its diagonal is √50 = 5√2.',
'geo-factoring':'x² + x − 6 = 0 factors as (x + 3)(x − 2) = 0. The solutions are x = −3 and x = 2.',
'geo-formula':'For x² − 2x − 3 = 0, a = 1, b = −2, c = −3. The formula gives x = (2 ± 4)/2 = 3 or −1.',
'geo-complete-square':'x² + 6x = 7. Add 9 to both sides: (x + 3)² = 16. Thus x = −3 ± 4 = 1 or −7.',
'geo-systems':'For y = x + 1 and x + y = 7, substitute: 2x + 1 = 7. Then x = 3 and y = 4. Check both original equations.',
'geo-points':'B is between A and C. If AB = 6 and AC = 17, then 6 + BC = 17, giving BC = 11.',
'geo-midpoints':'For A(−2,3) and B(4,−3), M = ((−2 + 4)/2, (3 − 3)/2) = (1,0).',
'geo-bisectors':'A bisector creates halves 3x + 1 and x + 9. Set them equal: 3x + 1 = x + 9. Then x = 4 and each half is 13.',
'geo-slope':'Through (1,2) and (3,8), m = (8 − 2)/(3 − 1) = 6/2 = 3. Through two points with the same x-coordinate, slope is undefined.',
'geo-line-equations':'Slope 2 through (3,7): 7 = 2(3) + b, so b = 1. The line is y = 2x + 1.',
'geo-angles':'Two adjacent angles measuring 28° and 47° form a 75° angle. The supplement of 75° is 180° − 75° = 105°.',
'geo-angle-bisector':'An angle bisector makes halves 3x + 5 and 5x − 15. Equate them: x = 10. Each half is 35°, so the whole angle is 70°.',
'geo-parallel':'For parallel lines, same-side interior angles 2x and 3x satisfy 2x + 3x = 180. Thus x = 36 and the angles are 72° and 108°.',
'geo-perpendicular':'A line perpendicular to y = 2x + 1 through (0,3) has slope −1/2, so its equation is y = −x/2 + 3.',
'geo-centers':'For the segment from (0,0) to (4,2), midpoint M = (2,1) and segment slope is 1/2. Its perpendicular bisector has equation y = −2x + 5.',
'geo-circumcenter':'A right triangle with vertices (0,0), (6,0), and (0,8) has circumcenter (3,4), the midpoint of its hypotenuse. Each vertex is 5 units from that center.',
'geo-angle-strategy':'Triangle angles x + 10, 2x, and 80° give 3x + 90 = 180. Then x = 30°, and the three angles are 40°, 60°, and 80°.'}
for t in T:
 for k in ['easy','medium','expert']:
  R[t['id']][k]['example']=examples[t['id']]
  R[t['id']][k]['desc']=R[t['id']][k]['parts'][0][1]
 t['example']=examples[t['id']];t['desc']=R[t['id']]['medium']['desc']
# New daily lessons have their own practice sets; old question indices remain stable.
for q in Q:
 if q['topic']=='geo-radical-operations':
  if 'Rationalize' in q['prompt']:q['topic']='geo-rationalize'
  elif 'multiply' in q['prompt'].lower() or '(√5' in q['prompt']:q['topic']='geo-radical-products'
 if q['topic']=='geo-centers':
  if 'incenter' in q['why'].lower():q['topic']='geo-angle-bisector'
  elif 'circumcircle' in q['prompt'].lower():q['topic']='geo-circumcenter'
 if q['topic']=='geo-angles' and 'bisector' in q['prompt'].lower():q['topic']='geo-angle-bisector'
def question(id,p,opts,a,why):Q.append({'topic':'geo-'+id,'prompt':p,'options':opts,'answer':a,'why':why})
for args in [
('radical-operations','Simplify 7√5 − 2√5.',['5','5√5','√5','9√5'],1,'Subtract the coefficients; keep the common radical: (7 − 2)√5 = 5√5.'),
('radical-operations','Which pair can be combined directly by adding coefficients?',['√2 and √3','2√7 and 5√7','√5 and 5','√2 and 2'],1,'The second pair has the same simplified radicand, 7.'),
('radical-products','Simplify √6 × √24.',['√30','6','12','24'],2,'√(6 × 24) = √144 = 12.'),
('radical-products','Simplify √75 ÷ √3.',['5','25','√78','√72'],0,'√(75/3) = √25 = 5.'),
('rationalize','Rationalize 1/(√5 + 1).',['(√5 + 1)/6','(√5 − 1)/4','√5 − 1','1/6'],1,'Multiply numerator and denominator by √5 − 1. The denominator becomes 5 − 1 = 4.'),
('rationalize','The conjugate of 3 − √2 is…',['−3 + √2','3 + √2','√3 − 2','3 − √2'],1,'A conjugate changes the sign between the same two terms.'),
('bisectors','A bisector makes segment halves 3x + 2 and x + 10. Find x.',['2','4','6','8'],1,'Set equal: 3x + 2 = x + 10, so 2x = 8 and x = 4.'),
('bisectors','A line bisects AB at M. If AM = 9, AB = ?',['4.5','9','18','27'],2,'AM = MB = 9, so AB = 18.'),
('bisectors','Does a segment bisector always meet the segment at 90°?',['Yes','Only if the segment is horizontal','No','Only on a grid'],2,'It must pass through the midpoint. Perpendicularity is an additional condition.'),
('angles','An angle of 125° is…',['Acute','Right','Obtuse','Straight'],2,'Obtuse angles are greater than 90° and less than 180°.'),
('angle-bisector','Angle halves are 2x + 5 and 3x − 10. Find x.',['5','10','15','20'],2,'Bisected angles are equal: 2x + 5 = 3x − 10 gives x = 15.'),
('centers','Every point on a perpendicular bisector is…',['Equidistant from the segment endpoints','A vertex','Inside a triangle','On the original segment'],0,'The perpendicular bisector is the set of points equally distant from both endpoints.'),
('centers','Perpendicular bisector of the segment (0,0) to (4,2)?',['y = 2x + 1','y = −2x + 5','y = x/2','x = 4'],1,'Midpoint (2,1), perpendicular slope −2: y − 1 = −2(x − 2), so y = −2x + 5.'),
('circumcenter','The circumcenter is the intersection of…',['Medians','Angle bisectors','Side perpendicular bisectors','Triangle sides'],2,'Side perpendicular bisectors meet at a point equidistant from all three vertices.'),
('circumcenter','Can a circumcenter be outside its triangle?',['Yes, for an obtuse triangle','No, never','Only for an equilateral triangle','Only for an acute triangle'],0,'An obtuse triangle has its circumcenter outside; the incenter stays inside.')]:question(*args)
# Fresh terms-only flashcards are authored separately, with explicit migration of old review IDs.
C=[]
Path('public/geometry-content.js').write_text('/* Geometry daily lessons follow uploaded packet order. */\nconst GEOMETRY='+json.dumps({'topics':T,'questions':Q,'cards':C,'reading':{t['id']:R[t['id']] for t in T}},ensure_ascii=False)+';\nTOPICS.push(...GEOMETRY.topics);QUESTIONS.push(...GEOMETRY.questions);\nObject.assign(READING_CONTENT.topics,GEOMETRY.reading);\n')
print(len(T),'Geometry daily lessons,',len(Q),'practice questions')
