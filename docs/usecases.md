---
hide:
  - navigation
  - toc
---

# Use Cases

Below are example research projects that demonstrate how the EDIA modules can be combined.

## Projects

<div class="grid cards grid--cols-2" markdown>

-   ![VRStereoFem](assets/thumbnail_vr2f.gif){ .usecase-thumb loading=lazy }  
    **EEG decodability of facial expressions and their stereoscopic depth cues in immersive virtual reality**  

    ??? info "Project details"
        **Summary**: The study integrates immersive virtual reality with EEG and eye tracking to examine face perception under controlled stereoscopic depth conditions. Using time-resolved multivariate decoding, EEG signals recorded in fully immersive VR reliably differentiated facial expressions. Stereoscopic depth cues elicit distinct, decodable neural signatures, while expression decoding remains robust across depth conditions, demonstrating the feasibility of multimodal decoding in 3D environments.  
        
        **Time**: 2022–2025  

        **Equipment**  

        - Platform: PC VR
        - Headset: HTC Vive Pro Eye
        - Interaction: HTC Vive Pro Controllers

        **Data modalities**

        - :fontawesome-solid-water: EEG  
        - :fontawesome-solid-eye: eye tracking   
        - :fontawesome-solid-gamepad: subjective reports  

        **EDIA Modules** [version]

        - {{ edia("core", version="pre-release") }}
        - {{ edia("eye", version="pre-release") }}
        - {{ edia("eye_vive", version="pre-release") }}

        **Publications & links** 

        - :fontawesome-solid-newspaper: [Paper [eLife]](https://elifesciences.org/reviewed-preprints/108933v1){:target="_blank"}
        - :fontawesome-brands-github: [GitHub repo](https://github.com/eioe/vr2f/){:target="_blank"}

-   ![Affective VR](assets/thumbnail_affecttracker.png){ .usecase-thumb loading=lazy }  
    **AffectTracker: real-time continuous rating of affective experience in immersive virtual reality**

    ??? info "Project details"
        **Summary**: Studying dynamics and physiology of affective states in immersive virtual reality. Emotion elicitation through stereoscopic 360° videos and simultaneous recordings of subjective ratings and multimodal physiological and eye tracking data.  

        **Time**: 2023–ongoing  

        **Equipment**

        - Platform: PC VR
        - Headset: HTC Vive Pro Eye
        - Interaction: HTC Vive Controllers

        **Data modalities**

        - :fontawesome-solid-water: EEG
        - :fontawesome-solid-heart: ECG
        - :fontawesome-solid-lungs: respiration
        - :fontawesome-solid-hand-holding-droplet: skin conductance
        - :fontawesome-solid-eye: eye tracking 
        - :fontawesome-solid-rotate: head tracking 
        - :fontawesome-solid-gamepad: subjective reports 

        **EDIA Modules** [version]

        - {{ edia("core", version="pre-release") }}
        - {{ edia("lsl", version="pre-release") }}
        - {{ edia("eye", version="pre-release") }}
        - {{ edia("eye_vive", version="pre-release") }}

        **Publications & links**

        - :fontawesome-solid-newspaper: [Paper [Front. Virtual Real.]](https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2025.1567854/full){:target="_blank"}
        - :fontawesome-brands-github: [GitHub – AffectTracker](https://github.com/afourcade/AffectTracker){:target="_blank"}
        - :material-open-in-new: [Thefirstfloor project page](https://www.behance.net/gallery/208265939/Affective-VR){:target="_blank"}

-   ![3DIL](assets/thumbnail_3dil.gif){ .usecase-thumb loading=lazy }  
    **Project 3DIL: Revolutionising Eyewitness Identification — The 3D Interactive Lineup**  

    ??? info "Project details"
        **Summary**: The 3D Interactive Lineups (3DIL) project is transforming eyewitness identification through the use of 3D virtual reality (VR). Traditional 2D photo lineups can often lead to mistaken identifications, contributing to wrongful convictions. Our innovative approach uses advanced 3D modeling and neural rendering to create lifelike, interactive facial models, allowing witnesses to view suspects from multiple angles in VR. This project brings together an international team of experts in psychology, computer science, and law enforcement to set a new standard in criminal justice procedures.  

        **Time**: 2024–ongoing 

        **Equipment**

        - Platform: PC VR
        - Headset: Varjo Aero
        - Interaction: HTC Vive Controllers

        **Data modalities**

        - :fontawesome-solid-eye: eye tracking 
        - :fontawesome-solid-gamepad: subjective reports 

        **EDIA Modules**  

        - {{ edia("core", version="pre-release") }}
        - {{ edia("eye", version="pre-release") }}
        - {{ edia("eye_varjo", version="pre-release") }}

        **Publications & links**

        - :material-open-in-new: [Project website](https://www.3dinteractivelineup.com/){:target="_blank"}

-   ![validet](assets/thumbnail_validet.gif){ .usecase-thumb loading=lazy }  
    **Scientific Eye Tracking Data Quality in immersive Virtual Reality: A Comparison of Tethered and Mobile VR Headsets** 

    ??? info "Project details"
        **Summary**: This study evaluates the eye-tracking performance of five state-of-the-art virtual reality (VR) headsets to assess their suitability for scientific research. Using data from 24 participants, the authors compare three mobile devices (Meta Quest Pro, PICO 4 Enterprise, HTC Vive Focus 3) and two tethered headsets (HTC Vive Pro Eye, Varjo Aero) on key performance metrics: spatial accuracy, precision, and temporal latency. Eye tracking was measured during fixation and saccade tasks performed with and without head movements, and latency was estimated relative to concurrently recorded electrooculography (EOG).

        **Time**: 2025–ongoing  

        **Equipment**

        - Platform: <span style="color:#4fc3f7;"> PC VR </span> | <span style="color:#a1887f;"> mobile VR </span>
        - Headset: <span style="color:#4fc3f7;"> HTC Vive Pro</span> | <span style="color:#4fc3f7;">Varjo Aero</span> | 
        <span style="color:#a1887f;">Meta Quest Pro</span> | <span style="color:#a1887f;"> HTC Vive Focus 3</span> | 
        <span style="color:#a1887f;"> PICO 4 Enterprise</span>
        - Interaction: Controllers

        **Data modalities**

        - :fontawesome-solid-eye: eye tracking 
        - :fontawesome-solid-arrows-to-eye: EOG 
        - :fontawesome-solid-rotate: head tracking

        **EDIA Modules**

        - {{ edia("core", version="v0.4") }}
        - {{ edia("eye", version="v0.0.1") }}
        - {{ edia("eye_varjo", version="exp-validet") }}
        - {{ edia("eye_vive", version="exp-validet") }}
        - {{ edia("eye_quest", version="exp-validet") }}
        - {{ edia("eye_pico", version="exp-validet") }}
        - {{ edia("eye_focus", version="exp-validet") }}
        - {{ edia("lsl", version="pre-release") }}
        - {{ edia("rcas", version="v0.4.0") }}

        **Publications & links**

        - :fontawesome-solid-person-chalkboard: [Meeting Abstract [VSS 2025]](https://jov.arvojournals.org/article.aspx?articleid=2809682){:target="_blank"}
        - :fontawesome-solid-person-chalkboard: [Poster [Psychologie & Gehirn 2025]](https://pure.mpg.de/rest/items/item_3674441_3/component/file_3674442/content){:target="_blank"}

-   ![TIDAL](assets/thumbnail_tidal.gif){ .usecase-thumb loading=lazy }  
    **TIDAL: Tracking Interpersonal Distance And Loneliness**  

    ??? info "Project details"
        **Summary**: A multimodal pilot study examining how loneliness relates to interpersonal distance preferences and cardiac autonomic responses in a social stop-distance paradigm delivered in immersive VR. Participants are approached by virtual agents while ECG and movement data are recorded; a 5-day ecological momentary assessment arm captures everyday social experience and affect. The study tests associations between interoception, loneliness, and cardiac responses to social proximity.

        **Time**: 2026–2028  

        **Equipment**

        - Platform: PC VR
        - Headset: Varjo Aero

        **Data modalities**

        - :fontawesome-solid-heart: ECG
        - :fontawesome-solid-person-walking: accelerometer
        - :fontawesome-solid-eye: eye tracking
        - :fontawesome-solid-mobile-screen: ecological momentary assessment
        - :fontawesome-solid-gamepad: subjective reports
        - :fontawesome-solid-clipboard-list: questionnaires

        **EDIA Modules**

        - {{ edia("core", version="v0.6.1") }}
        - {{ edia("eye", version="v0.6.0") }}
        - {{ edia("eye_varjo", version="pre-release") }}
        - {{ edia("lsl", version="v0.6.1") }}

        **Publications & links**

        - :fontawesome-brands-github: [GitHub repo](https://github.com/alekspiejka/TIDAL){:target="_blank"}

-   ![SpaceVR](assets/thumbnail_spacevr.gif){ .usecase-thumb loading=lazy }  
    **SpaceVR: Idiothetic cue availability and spatial memory formation in immersive virtual reality in adolescence**  

    ??? info "Project details"
        **Summary**: The SpaceVR study investigates how idiothetic cues contribute to spatial memory above and beyond visual cues in adolescents. Using a within-subjects mobile VR paradigm, participants complete matched path integration and spatial memory tasks under two conditions: free walking or seated and controller-based. The study illuminates the developmental sequence in which distance and angular estimation mature as a function of cue availability and are integrated with visual information to refine spatial memory accuracy.

        **Time**: 2026–ongoing  

        **Equipment**

        - Platform: PC VR
        - Headset: Meta Quest Pro
        - Interaction: Meta Quest Touch Pro Controllers

        **Data modalities**

        - :fontawesome-solid-rotate: head tracking
        - :fontawesome-solid-eye: eye tracking

        **EDIA Modules**

        - {{ edia("core", version="v0.6.1") }}
        - {{ edia("eye", version="v0.6.0") }}
        - {{ edia("eye_quest", version="exp-validet") }}

        **Publications & links**: TBA

</div>
