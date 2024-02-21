(() => {
    const cards = `Dophan
  Duende
  Elfo Bardo
  Gorad Menor
  Guerrero Menor
  Mel
  Mimit
  Poder
  Aries Menor
  Guarda
  Guerrero Mediano
  Lestat
  Ninfa
  Ozk
  Aries Mediano
  Atia
  Chapanhan
  Eio Menor
  Enano Menor
  Explorador
  Gorad Mediano
  Bashi
  Enano Mayor
  Golem
  Gorad Mayor
  Lancero
  Momia
  Orco
  Aries Mayor
  Arlequin Menor
  Celestial
  Chamad
  Eio Mayor
  Mercenario
  Poder x 3
  Zoa
  Arlequin Mayor
  Atea
  Ave de noche
  Elfo Negro
  Escudal
  Fuente de vida
  Minotauro
  Paleo
  Poderador
  Radia
  Rukia
  Umbral
  Blitz Menor
  Cobald
  Gran Elfo
  Gran Guerrero
  Gusold
  Mago Blanco
  Oratio
  Ordrihn
  Poder x 4
  Rush
  Veneno
  Ador
  Atriad
  Blitz Mediano
  Drenador
  Enano de Oro
  Eretik
  Hada
  Hidra
  Mercane
  Trasgo Menor
  Bebe Dragon
  Blitz Mayor
  Lancero Menor
  Moriel
  Mujer Aguila
  Oracty
  Tachi
  Aguila Gigante
  Arpada
  Dehil
  Fureh
  Gran Oso
  Poder x 5
  Suza
  Vampiro
  Veneno x 2
  Demonio
  Gran Blitz
  Hongo
  Malar
  Mole
  Sardo
  Sombra
  Trasgo Mayor
  Elfo Arquero
  Escudal x 2
  Fuente de vida x 2
  Gran Trasgo
  Hombre Lobo
  Lancero Mayor
  Presenter
  Arcero
  Hyel
  Inevitables
  Lanzador
  Poder Mental
  Poder x 6
  Poderador x 2
  Taros
  Tumbadil
  Azote
  Dragon Rojo
  Ithids Menores
  Korth
  Morthen
  Oscuro
  Albala
  Atea Mayor
  Barrera Mistica
  Basilisco
  Escudal x 3
  Ithids Mayores
  Poder x 7
  Poder x 7 Ametal
  Poder x 7 Domica
  Poder x 7 Natural
  Poder x 7 Poderal
  Sirena
  Thrul
  Urgul
  Colossus
  Espinal
  Kurth Arth
  Poder Mental x 2
  Saga
  Astral
  Drenador x 2
  Elfo Avanzado
  Esteagol
  Muralez
  Osgo
  Poder x 8 Mayor
  Viguil
  Alchemia
  Kehanar
  Petioner
  Trigild
  Barbaro
  Poderador x 3
  Tutar Amon
  Veneno x 3
  Yogoloth
  Angel Caido
  Argnathor Poderal
  Fuente de vida x 3
  Manath
  Observador
  Poder Mental x 3
  Poder Mental x 4
  Poder x 10
  Poder x 10 Ametal
  Poder x 10 Domica
  Poder x 10 Natural
  Poder x 10 Poderal
  Rebolt
  Urgul Mayor
  Acrum
  Arienel
  Escudal x 4
  Alendrar
  Barrera Mistica x 2
  Dragon esqueleto
  Drakar
  Elfo Oscuro
  Kurth Arth x 2
  Poder Mental x 5
  Poder x 12 Mayor
  Afal
  Drenador x 3
  Dragor
  Grifo
  Argnathor Ametal
  Chimera Menor
  Enher
  Fuente de vida x 4
  Paladin
  Poder x 15
  Poder x 15 Ametal
  Poder x 15 Domica
  Poder x 15 Natural
  Poder x 15 Poderal
  Poderador x 4
  Rueda
  Ruinthz
  Titan
  Acrum x 2
  Draconia
  Espiritu del mar
  Maderal
  Muralez x 2
  Corrosivo
  Hermanos Elfo
  Kraken
  Poder Mental x 6
  Poder Mental x 7
  Mohrg
  Servidor
  Arcangel
  Demonio rojo
  Flora
  Veneno x 4
  Archer
  Argnathor Natural
  Caza Dragones
  Hechizero Negro
  Hombre Angel
  Poder x 15 Mayor
  Gith
  HipoGrifo
  Solemn
  Chimera Mayor
  Elion
  Kurth Arth x 3
  Poder Mental x 8
  Dragon azul
  Dragon verde
  Escudal x 5
  Acrum x 3
  Ardala
  Dragon Helado
  Gargola
  Argnathor Domic
  Barrera Mistica x 3
  Elfo Brujo
  Fuente de vida x 5
  Gargola de Oro
  Incael
  Rueda x 2
  Sanal
  Poder Mental x 9
  Poderador x 5
  Remente
  Ruinthz x 2
  Sibad
  Agathirmur
  Rataria
  Fase
  Garbol
  Hijo de Keathan
  Krahn
  Veneno x 5
  Athar Zum
  Bestia del Caos
  Drac Azul Mayor
  Drac Blanco Mayor
  Dragon Marron
  Tormentus
  Drac de Bronce
  Dragon Dorado
  Ruinthz x 3
  Asxel
  Dragon Plateado
  Kurth Arth x 4
  Rueda x 3
  Stazhart
  Angrath
  GraDrac
  Drac Verde Mayor
  Volatilh
  Acrum x 4
  Gigante
  Grath
  Insignia Solamnica
  Poder Mental x 10
  Genios
  Imnazthril
  Oroth Fezhal
  Dragon Demonio
  Dragon Negro
  Pesadilla
  Reptenzh
  Dragon Oscuro
  Poder Mental x 11
  Tentaculo
  Keatahn
  Poder x 20`
    
    let images = '';
    
    const out = cards.split('\n').map((item, index) => {
        const filename = item.trim()
            .toLowerCase()
            .replaceAll(' x ', '')
            .replaceAll(' ', '_')
            .replaceAll('_de_', '_')
            .replaceAll('_del_', '_');
        
        const element = {
        id: index,
        name: item,
        images: {
            small: {
              original: `crt_${filename}.jpg`,
              sanitized: `${index}_s.jpg`
            },
            horizontal: {
              original: `crt_${filename}_h.jpg`,
              sanitized: `${index}_h.jpg`
            },
            full: {
              original: `crt_${filename}_g.jpg`,
              sanitized: `${index}.jpg`
              }
            }
        };
        
        images += element.images.full.original + '\n';
        
        return element;
    });


    console.log(images);
    console.log(JSON.stringify(out));
  })();