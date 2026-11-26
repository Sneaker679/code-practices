# Who Wrote This?! (It Was Me)

*Practices and principles for code that lasts*

A 40-minute Beamer talk for graduate researchers in physics who write code but
were never taught how to design it. It starts from real failures and bad
habits, explains what makes code hard to change, then covers basic good
practices and the essential GRASP and SOLID design principles. All examples are
short before/after Python snippets drawn from classical mechanics.

## Project layout

```
main.tex               preamble, title, list of sections
beamerthemetalk.sty    the theme: colours, fonts, templates and slide commands (thanks claude)
references.bib         sources cited on the slides
sections/              one file per section, in order
  unused-slides.tex    slides kept for reference, not included
code/                  every Python snippet shown on a slide, one file each
diagrams/              PlantUML sources (*.puml) and their TikZ exports (out/)
images/                pictures (\graphicspath points here)
```

## Theme

Switch the whole deck between dark and light in `main.tex`:

```latex
\usetheme[dark]{talk}    % or [light]
```

A single slide can use the other theme by wrapping it in braces:

```latex
{\lighttheme
\begin{frame}{Title} ... \end{frame}
}
```

### Slide commands

| Command | Effect |
|---|---|
| `\takeaway{text}` | The slide's main message, centred in the accent colour |
| `\beforelabel`, `\afterlabel` | Red "Before" and green "After" badges |
| `\inputminted{python}{code/...}` | A code file in a rounded box |
| `\source{key}` | Cite a source in the slide's footer (author, year, title) |
| `\sectionquestion{text}` | Guiding question on the next section divider (put it before `\section`) |
| `\bigstat{figure}{caption}` | Large red figure with a caption |
| `\diagram[height]{file}` | Insert a PlantUML export, shrunk to fit |
| `\foldlines{start}{length}`, `\fold` | Fake a collapsed function in a code block |
| `\cutoff{label}` | Fade out content that runs off the bottom of a slide |

## Diagrams

Diagrams are written in PlantUML and share `diagrams/theme.puml`, which matches
the slide colours. Each diagram is exported as TikZ to
`diagrams/out/<name>/<name>.latex` and included with `\diagram`.

Diagrams use the dark palette by default. For the light theme, add
`!$dark = %false()` before the `!include theme.puml` line and export again.

## License

© 2026 Benjamin Gauthier.

| What | License |
|---|---|
| Slides, text and diagrams (`main.tex`, `sections/`, `diagrams/`, `references.bib`) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), see [`LICENSE`](LICENSE) |
| Code and theme (`code/`, `beamerthemetalk.sty`) | [MIT](https://opensource.org/licenses/MIT), see [`LICENSE-CODE`](LICENSE-CODE) |

Third-party material is not covered by these licenses:

- The image on the closing slide is not included in the repository. Without it,
  the slide shows a placeholder.
- The "Why bother with design?" chart is redrawn from Martin Fowler's
  [Design Stamina Hypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html)
  and credited on the slide.
- Facts and figures about the Toyota, CrowdStrike and Chang cases come from the
  sources cited on each slide.
