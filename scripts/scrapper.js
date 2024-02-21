// Example out CSV
// http://web.archive.org/web/20021231221705/http://www.rolplay.net/eljuego/cartas_lista.asp?coleccion=Todas&nivel=11
/*
Trasgo Mayor;80;2;11
Gran Blitz;10;2;11
Sombra;60;2;11
Mole;65;2;11
Demonio;75;2;11
Sardo;30;2;11
Hongo;99;2;11
Malar;90;2;11
*/

(() => {
    const level = 10;
    let out = "";
    
    const cards = Array.from(document.getElementsByTagName('td')).map(item => {
      const components = item.innerText.trim().split('\n');
      
      // Check if this is not a page layout
      if (components.length != 4) {
             return null;   
      }
      
      const card = {
        name: components[0].trim(),
        rarity: parseInt(components[2].replaceAll("Rareza:", "").trim()),
        quantity: parseInt(components[3].replaceAll("Nº por baraja:", "").trim()),
        level: level
      };
      
      return card;
    }).filter(item => item != null).map(item => {
      out += `${item.name};${item.rarity};${item.quantity};${item.level}\n`;
      return item;
    });
     
      console.log('Total Cards:', cards.length);
      console.log(out);
})();
    

