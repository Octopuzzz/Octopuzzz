<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="900" height="480"
     role="img" aria-label="Reagent Sandra — backend and streaming data engineer, Jakarta, Indonesia">
  <title>Reagent Sandra — backend &amp; streaming data</title>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1A1147"/>
      <stop offset="55%" stop-color="#130D33"/>
      <stop offset="100%" stop-color="#0C0822"/>
    </linearGradient>

    <radialGradient id="auroraA" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF4D8D" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FF4D8D" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraB" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38E8C8" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#38E8C8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="auroraC" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7C5CFF" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#7C5CFF" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="spectrum" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FF4D8D"/>
      <stop offset="38%" stop-color="#7C5CFF"/>
      <stop offset="72%" stop-color="#38E8C8"/>
      <stop offset="100%" stop-color="#FFA23E"/>
    </linearGradient>

    <!-- userSpaceOnUse so the wash runs across the whole portrait, not per row -->
    <linearGradient id="portrait" gradientUnits="userSpaceOnUse"
                    x1="0" y1="122" x2="0" y2="378">
      <stop offset="0%" stop-color="#FF9BC4"/>
      <stop offset="42%" stop-color="#BCA6FF"/>
      <stop offset="100%" stop-color="#7BFFE4"/>
    </linearGradient>

    <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>

    <filter id="haze" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="46"/>
    </filter>
    <filter id="spark" x="-160%" y="-160%" width="420%" height="420%">
      <feGaussianBlur stdDeviation="3.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="card"><rect width="900" height="480" rx="24"/></clipPath>
    <clipPath id="artclip">
      <rect x="38" y="110" width="304" height="276"/>
    </clipPath>
  </defs>

  <style>
    .sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter,
                          Roboto, "Helvetica Neue", Arial, sans-serif; }
    .mono { font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo,
                          Consolas, "Liberation Mono", monospace; }
    .eyebrow { font-size: 11px; letter-spacing: 2.6px; fill: #38E8C8; }
    .name    { font-size: 42px; font-weight: 800; fill: #F7F5FF; letter-spacing: -0.5px; }
    .role    { font-size: 15.5px; fill: #B5ADE0; }
    .chip    { font-size: 12px; fill: #DAD5F7; }
    .stage   { font-size: 11.5px; fill: #CFC9F0; }
    .quiet   { font-size: 10px; letter-spacing: 2.4px; fill: #8A80C2; }
    .art     { font-size: 5.30px; fill: url(#portrait); opacity: 1;
                white-space: pre; }

    .packet { animation: flow 3.6s linear infinite; }
    .p2 { animation-delay: 0.9s; }
    .p3 { animation-delay: 1.8s; }
    .p4 { animation-delay: 2.7s; }
    .node { animation: breathe 3.6s ease-in-out infinite; }
    .n1 { animation-delay: 0.9s; }
    .n2 { animation-delay: 1.8s; }
    .n3 { animation-delay: 2.7s; }
    #sweep { animation: scan 5s ease-in-out infinite; }

    @keyframes flow {
      0%   { transform: translateX(0px); opacity: 0; }
      6%   { opacity: 1; }
      94%  { opacity: 1; }
      100% { transform: translateX(432px); opacity: 0; }
    }
    @keyframes breathe {
      0%, 100% { opacity: 0.30; }
      12%      { opacity: 0.85; }
      40%      { opacity: 0.30; }
    }
    @keyframes scan {
      0%   { transform: translateY(0px); }
      100% { transform: translateY(256px); }
    }

    @media (prefers-reduced-motion: reduce) {
      .packet { animation: none; opacity: 0.9; }
      .node   { animation: none; opacity: 0.5; }
      #sweep  { animation: none; opacity: 0; }
    }
  </style>

  <g clip-path="url(#card)">
    <rect width="900" height="480" fill="url(#bg)"/>

    <g filter="url(#haze)">
      <ellipse cx="742" cy="10" rx="250" ry="170" fill="url(#auroraA)"/>
      <ellipse cx="898" cy="250" rx="200" ry="180" fill="url(#auroraC)"/>
      <ellipse cx="150" cy="470" rx="250" ry="170" fill="url(#auroraB)"/>
    </g>

    <!-- portrait -->
    <rect x="28" y="98" width="324" height="302" rx="18"
          fill="#FFFFFF" fill-opacity="0.035" stroke="#FFFFFF" stroke-opacity="0.09"/>
    <g clip-path="url(#artclip)">
      <text class="art" x="48" y="134.21" textLength="162.2" lengthAdjust="spacing" xml:space="preserve">                                     .::-----~---:.</text>
      <text class="art" x="48" y="140.32" textLength="174.9" lengthAdjust="spacing" xml:space="preserve">                                  -=+=~:::::---::-~===.</text>
      <text class="art" x="48" y="146.42" textLength="181.3" lengthAdjust="spacing" xml:space="preserve">                               ,==-::::::::::::::::::~==:</text>
      <text class="art" x="48" y="152.53" textLength="187.6" lengthAdjust="spacing" xml:space="preserve">                             ,==::::::::::::::::::::::::~+,</text>
      <text class="art" x="48" y="158.63" textLength="190.8" lengthAdjust="spacing" xml:space="preserve">                           .+=:::::::---=+++==~~--::::::::==</text>
      <text class="art" x="48" y="164.74" textLength="197.2" lengthAdjust="spacing" xml:space="preserve">                          :+::::::-+8M#%@@@@@@%%#M&amp;*=-:::::-+,</text>
      <text class="art" x="48" y="170.84" textLength="200.3" lengthAdjust="spacing" xml:space="preserve">                         .*:::::-+M%@@@@@@@@@@@@@@@@%W*-:::::*.</text>
      <text class="art" x="48" y="176.95" textLength="200.3" lengthAdjust="spacing" xml:space="preserve">                         :~::::~8W@@@@@@@@@@@@@@@@@@@@%B=::::~-</text>
      <text class="art" x="48" y="183.06" textLength="200.3" lengthAdjust="spacing" xml:space="preserve">                         :~:::=B#@@@@@@@@@@@@@@@@@@@@@@@#=:::--</text>
      <text class="art" x="48" y="189.16" textLength="200.3" lengthAdjust="spacing" xml:space="preserve">                         ,+::-*#@@@@@%@@@@@@@@@@@@@@@@@@@B-::=:</text>
      <text class="art" x="48" y="195.27" textLength="197.2" lengthAdjust="spacing" xml:space="preserve">                          *::=%@@@%#%##@@@@@@@@@@@%###%@@%=::*</text>
      <text class="art" x="48" y="201.37" textLength="197.2" lengthAdjust="spacing" xml:space="preserve">                          ,+~*@@%WWMBB88B#%@@@#MB8&amp;8M#WB#@B:=-</text>
      <text class="art" x="48" y="207.48" textLength="194.0" lengthAdjust="spacing" xml:space="preserve">                           ~*8%WB#%WWMBBM%MW#WWMB88MBW#WM##*B</text>
      <text class="art" x="48" y="213.58" textLength="197.2" lengthAdjust="spacing" xml:space="preserve">                           B*B@@#%#&amp;8&amp;*B&amp;MMM%8MM&amp;&amp;*M*8##%@#&amp;M,</text>
      <text class="art" x="48" y="219.69" textLength="194.0" lengthAdjust="spacing" xml:space="preserve">                           *WM@@%#@%#%##WWMW%WMW##%%#%%#@##M&amp;</text>
      <text class="art" x="48" y="225.80" textLength="194.0" lengthAdjust="spacing" xml:space="preserve">                           ,MB@%@%%%%%%#MBW%%WMBW#%%#%%@@#WM,</text>
      <text class="art" x="48" y="231.90" textLength="190.8" lengthAdjust="spacing" xml:space="preserve">                            8M%%@%@@@@@8MW#%%###B#@@@@@%%WM&amp;</text>
      <text class="art" x="48" y="238.01" textLength="190.8" lengthAdjust="spacing" xml:space="preserve">                            -W##%%@@@@@##WW##WW#W@@@@@%%#WW~</text>
      <text class="art" x="48" y="244.11" textLength="187.6" lengthAdjust="spacing" xml:space="preserve">                             ~M#%%@@@@@%#%######%@@@@@%#WB-</text>
      <text class="art" x="48" y="250.22" textLength="184.4" lengthAdjust="spacing" xml:space="preserve">                              :#%%@@@@@B8+*&amp;&amp;**&amp;8#@@@%%%W:</text>
      <text class="art" x="48" y="256.32" textLength="181.3" lengthAdjust="spacing" xml:space="preserve">                               *%@@@@@%B8BMMBBBMW%@@@@%W&amp;</text>
      <text class="art" x="48" y="262.43" textLength="181.3" lengthAdjust="spacing" xml:space="preserve">                                M%%@@@@@@%%#%%@@@@@@%#MM.</text>
      <text class="art" x="48" y="268.53" textLength="178.1" lengthAdjust="spacing" xml:space="preserve">                               :&amp;##W#%@@@@@@@@@@@%#WMMM*</text>
      <text class="art" x="48" y="274.64" textLength="181.3" lengthAdjust="spacing" xml:space="preserve">                              +~&amp;%%WWMW##%@@@@%#WB8BMWWM-</text>
      <text class="art" x="48" y="280.75" textLength="187.6" lengthAdjust="spacing" xml:space="preserve">                            ,+--W%@@%#WMB88BB8888BMW###B~+.</text>
      <text class="art" x="48" y="286.85" textLength="190.8" lengthAdjust="spacing" xml:space="preserve">                          .==::-%@@@@@@@%#######%%%%@@@*::+~</text>
      <text class="art" x="48" y="292.96" textLength="200.3" lengthAdjust="spacing" xml:space="preserve">                       .-==:::::B@@@@@@@@@@@@@@@@@@@@@%-:::-+-,</text>
      <text class="art" x="48" y="299.06" textLength="219.4" lengthAdjust="spacing" xml:space="preserve">                  ,:-~=~-:::::::~#@%@@@@@@%%%%@@%@@@@@+::::::-~=~~--,</text>
      <text class="art" x="48" y="305.17" textLength="235.3" lengthAdjust="spacing" xml:space="preserve">              :~==~-:::::::::::::~%@@@@@@@@@@@@@@@@%%=::::::::::::::-==~~:</text>
      <text class="art" x="48" y="311.27" textLength="248.0" lengthAdjust="spacing" xml:space="preserve">          :~==--::::::::::::::::::+%@@@@@@@@@@@@@@@W~:::::::::::::::::::-~==~:</text>
      <text class="art" x="48" y="317.38" textLength="260.8" lengthAdjust="spacing" xml:space="preserve">      ,-==-:::::::::::::::::::::-::-&amp;#@@@@@@@@@@@%&amp;-:::::::::::::::::::::::::-==~,</text>
      <text class="art" x="48" y="323.48" textLength="267.1" lengthAdjust="spacing" xml:space="preserve">    ~+~::::::::-:::::-::::::::::::::::+W@@@@@@@@8-::::::::::::::::::::::::::::::-=+~</text>
      <text class="art" x="48" y="329.59" textLength="273.5" lengthAdjust="spacing" xml:space="preserve">  ~+-::::::-::::-:::::::::::::::::::::::=8#%@@B~:::::::::::::::::::::::::::::::::::-+~</text>
      <text class="art" x="48" y="335.70" textLength="279.8" lengthAdjust="spacing" xml:space="preserve"> +~::::::::---::-::::::::::::::::::::::::::~=-::::::::::::::::::::::::::::::::::::::-~*.</text>
      <text class="art" x="48" y="341.80" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">+~:::::-::-----:::--::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-+</text>
      <text class="art" x="48" y="347.91" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">--::-:--::---------:-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-</text>
      <text class="art" x="48" y="354.01" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">-----:--::--------::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</text>
      <text class="art" x="48" y="360.12" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">-::---::::---:::----::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-:::</text>
      <text class="art" x="48" y="366.22" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">::::---:::---:------:::-:::::::::::::::::-::::--::::::::::::::::::::::::::::::::::::::::</text>
      <text class="art" x="48" y="372.33" textLength="279.8" lengthAdjust="spacing" xml:space="preserve">:::::--:::---::::-:---:::::::::::::::::-:-::::--::-:::::::::::::::::::::::::::::::::::::</text>
      <rect id="sweep" x="38" y="110" width="304" height="26" fill="url(#beam)"/>
    </g>

    <!-- identity -->
    <text class="mono eyebrow" x="372" y="100">SOFTWARE DEVELOPER · DATA STREAMING</text>
    <text class="sans name" x="372" y="150">Reagent Sandra</text>
    <rect x="372" y="168" width="66" height="4" rx="2" fill="url(#spectrum)"/>
    <text class="sans role" x="372" y="206">Backend and streaming data — Go, Kafka,</text>
    <text class="sans role" x="372" y="228">and the pipelines that run between them.</text>

    <g>
      <rect x="372" y="254" width="105" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.06" stroke="#FFFFFF" stroke-opacity="0.13"/><text class="mono chip" x="425" y="272" text-anchor="middle">Jakarta, ID</text>
      <rect x="487" y="254" width="127" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.06" stroke="#FFFFFF" stroke-opacity="0.13"/><text class="mono chip" x="551" y="272" text-anchor="middle">Bank Indonesia</text>
      <rect x="624" y="254" width="134" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.06" stroke="#FFFFFF" stroke-opacity="0.13"/><text class="mono chip" x="691" y="272" text-anchor="middle">BINUS · CS 3.59</text>
    </g>

    <line x1="372" y1="316" x2="856" y2="316" stroke="url(#rule)" stroke-width="1"/>
    <text class="mono quiet" x="372" y="342">PIPELINE</text>

    <!-- signature: the stream -->
    <g>
      <line x1="406" y1="382" x2="838" y2="382"
            stroke="url(#spectrum)" stroke-width="2" stroke-linecap="round" opacity="0.30"/>
      <g class="node"><circle cx="406" cy="382" r="14" fill="none" stroke="#FF4D8D" stroke-width="1.5"/></g><circle cx="406" cy="382" r="6" fill="#FF4D8D"/><text class="mono stage" x="406" y="412" text-anchor="middle">CDC</text>
      <g class="node n2"><circle cx="550" cy="382" r="14" fill="none" stroke="#7C5CFF" stroke-width="1.5"/></g><circle cx="550" cy="382" r="6" fill="#7C5CFF"/><text class="mono stage" x="550" y="412" text-anchor="middle">Kafka</text>
      <g class="node n3"><circle cx="694" cy="382" r="14" fill="none" stroke="#38E8C8" stroke-width="1.5"/></g><circle cx="694" cy="382" r="6" fill="#38E8C8"/><text class="mono stage" x="694" y="412" text-anchor="middle">ksqlDB</text>
      <g class="node n4"><circle cx="838" cy="382" r="14" fill="none" stroke="#FFA23E" stroke-width="1.5"/></g><circle cx="838" cy="382" r="6" fill="#FFA23E"/><text class="mono stage" x="838" y="412" text-anchor="middle">Analytics</text>
      <g filter="url(#spark)">
        <circle class="packet" cx="406" cy="382" r="4" fill="#FFE9F2"/>
        <circle class="packet p2" cx="406" cy="382" r="4" fill="#E4DBFF"/>
        <circle class="packet p3" cx="406" cy="382" r="4" fill="#D6FFF5"/>
        <circle class="packet p4" cx="406" cy="382" r="4" fill="#FFEFD9"/>
      </g>
    </g>
  </g>

  <rect x="0.5" y="0.5" width="899" height="479" rx="24"
        fill="none" stroke="#FFFFFF" stroke-opacity="0.10"/>
</svg>
