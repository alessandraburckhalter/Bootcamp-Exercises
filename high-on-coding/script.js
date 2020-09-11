const container = document.getElementById("container");

document.body.style.fontFamily = "sans-serif";

const header = document.createElement("header");
header.style.color = "white";
header.style.backgroundColor = "Blue";
header.style.display = "flex";
header.style.padding = "6px 20px";
header.style.marginTop = "26px";
container.appendChild(header);

const heading1 = document.createElement("h1");
heading1.textContent = "HighOnCoding";
heading1.style.fontSize = "36px";
heading1.style.paddingRight = "40px";
heading1.style.fontWeight = "600";
header.appendChild(heading1);

const nav1 = document.createElement("nav");
nav1.style.display = "flex";
nav1.style.alignItems = "center";
header.appendChild(nav1);

const anAnchor = document.createElement("a");
anAnchor.textContent = "Home";
anAnchor.href = "#";
anAnchor.style.paddingRight = "40px";
anAnchor.style.color = "white";
anAnchor.style.fontWeight = "bold";
anAnchor.style.fontSize = "24px";
anAnchor.style.textDecoration = "none";
nav1.appendChild(anAnchor);

const anAnchor1 = document.createElement("a");
anAnchor1.textContent = "Categories";
anAnchor1.style.fontSize = "24px";
anAnchor1.style.textDecoration = "none";
anAnchor1.href = "#";
anAnchor1.style.color = "white";
anAnchor1.style.fontWeight = "100";
nav1.appendChild(anAnchor1);

const main = document.createElement("main");
main.style.display = "flex";
main.style.flexDirection = "column";
main.style.alignItems = "center";
container.appendChild(main);

const div1 = document.createElement("div");
div1.style.display = "flex";
div1.style.flexDirection = "column";
div1.style.width = "90%";
div1.style.paddingLeft = "20px";
div1.style.paddingRight = "20px";
div1.style.marginTop = "20px";
div1.style.backgroundColor = "dddee0"
main.appendChild(div1);

const heading2 = document.createElement("h2");
heading2.textContent = "Curse of the Current Reviews";
heading2.style.fontSize = "30px";
heading2.style.color = "#54585e";
div1.appendChild(heading2);

const div1Paragraph = document.createElement("p");
div1Paragraph.textContent = "When you want to buy any application from the Apple iTunes store you have more choices than you can handle. Most of the users scroll past the application description completely avoiding it like ads displayed on the right column of your webpage. Their choice is dependent on three important factors price, screenshot and reviews."
div1Paragraph.style.fontSize = "14px";
div1.appendChild(div1Paragraph);

const section = document.createElement("section");
section.style.display = "flex";
section.style.flexDirection = "column";
section.style.maxWidth = "92%";
section.style.justifyContent = "center";
main.append(section);

const div2 = document.createElement("div");
div2.style.width = "100%";
section.append(div2);

const heading3 = document.createElement("h3");
heading3.textContent = "Hello WatchKit";
heading3.style.color = "2866ba";
heading3.style.fontWeight = "400";
heading3.style.paddingLeft = "5px"
heading3.style.marginTop = "20px";
heading3.style.marginBottom = "0px";
heading3.style.fontSize = "24px";
div1.append(heading3);

const paragraph1 = document.createElement("p");
paragraph1.textContent = "Last month Apple released the anticipated WatchKit Framework for developers in the form of iOS 8.2 beta SDK release. The WatchKit framework enable the developers to create Apple Watch applications. In this article we are going to focus on the basics of getting started with the WatchKit framework and developing apps for the Apple Watch."
paragraph1.style.paddingLeft = "5px";
paragraph1.style.fontSize = "14px";
paragraph1.style.marginTop = "10px";
paragraph1.style.marginBottom = "5px";
div1.append(paragraph1);

const bottomDiv = document.createElement("div");
bottomDiv.style.color = "white";
bottomDiv.style.backgroundColor = "#ff9900";
bottomDiv.style.display = "flex";
bottomDiv.style.padding = "5px";
bottomDiv.style.marginTop = "0px";
bottomDiv.style.fontWeight = "500";
div1.append(bottomDiv)

const textLeft = document.createElement("div");
textLeft.textContent = "12 comments";
bottomDiv.append(textLeft);

const textRight = document.createElement("div");
textRight.textContent = "124 Likes";
textRight.style.paddingLeft = "40px";
bottomDiv.append(textRight);

const div3 = document.createElement("div");
div3.style.width = "100%";
section.append(div3)

const heading4 = document.createElement("h4");
heading4.textContent = "Introduction to Swift";
heading4.style.fontWeight = "400";
heading4.style.paddingLeft = "5px"
heading4.style.marginTop = "20px";
heading4.style.marginBottom = "0px";
heading4.style.fontSize = "24px";
heading4.style.color = "2866ba";
div3.append(heading4);

const paragraph2 = document.createElement("p");
paragraph2.textContent = "Swift is a modern programming language developed by Apple to create the next generation of iOS and OSX applications. Swift is a  fairly new language and still in development but it clearly reflects the intentions and the future direction. This article will revolve around the basic concepts in the Swift language and how you can get started."
paragraph2.style.paddingLeft = "5px";
paragraph2.style.fontSize = "14px";
paragraph2.style.marginTop = "10px";
paragraph2.style.marginBottom = "5px";
div3.append(paragraph2);

const bottomDiv1 = document.createElement("div");
div3.append(bottomDiv1);
const textLeft2 = document.createElement("div");
textLeft2.textContent = "15 comments"
bottomDiv1.style.color = "white";
bottomDiv1.style.backgroundColor = "#ff9900";
bottomDiv1.style.display = "flex";
bottomDiv1.style.padding = "5px";
bottomDiv1.style.marginTop = "0px";
bottomDiv1.style.fontWeight = "500";
bottomDiv1.append(textLeft2);

const textRight2 = document.createElement("div");
textRight2.textContent = "45 Likes"
textRight2.style.paddingLeft = "40px";
bottomDiv1.append(textRight2);
bottomDiv1.style.backgroundColor = "orange";