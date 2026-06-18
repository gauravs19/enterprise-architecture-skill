workspace "<System Name>" "<one-line description>" {

    model {
        # --- people ---
        user = person "<User / Role>" "<what they do>"

        # --- the system in scope ---
        system = softwareSystem "<System Name>" "<purpose>" {
            web = container "Web Application" "<purpose>" "<tech>"
            api = container "API" "<purpose>" "<tech>"
            db  = container "Database" "<purpose>" "<tech>" {
                tags "Database"
            }

            web -> api "Makes calls to" "JSON/HTTPS"
            api -> db  "Reads/writes" "<driver>"
        }

        # --- external systems ---
        ext = softwareSystem "<External System>" "<purpose>" {
            tags "External"
        }

        # --- relationships ---
        user -> web "Uses" "HTTPS"
        api  -> ext "Integrates with" "<protocol>"
    }

    views {
        systemContext system "Context" {
            include *
            autolayout lr
        }
        container system "Containers" {
            include *
            autolayout lr
        }
        # component <container> "<Name>" { include * ; autolayout lr }

        styles {
            element "Person"   { shape person ; background #08427b ; color #ffffff }
            element "External" { background #999999 ; color #ffffff }
            element "Database" { shape cylinder }
        }
    }
}
